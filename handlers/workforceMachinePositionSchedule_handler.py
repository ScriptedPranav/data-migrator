from datetime import datetime, timedelta

from utils.api_caller import get_api
from mappings.sheet_api_endpoints import SHEET_API_ENDPOINTS
from config import START_DATE, END_DATE
from handlers.base_handler import BaseHandler

class WorkforceMachinePositionScheduleHandler(BaseHandler):
    
    def __init__(self, data, logger=None):
        super().__init__(data, logger)
        
    def manipulate_data(self):
        
        schedules = []
        for row in self.data:
            
            row["workforceId"] = str(int(row["workforceId"]))
            workforce_id = row["workforceId"]
            
            day_machine_position_mapping = self.get_day_machine_position_mapping(row)
            data = self.generate_schedules(workforce_id, START_DATE, END_DATE, day_machine_position_mapping)
            
            for schedule in data:
                schedules.append(schedule)
                
        self.schedules = schedules
        return self.schedules
    
    def get_day_machine_position_mapping(self, row) -> dict[str, str]:
        day_machine_position_mapping = {}
        
        day_machine_position_mapping["sun"] = row["Sun"]
        day_machine_position_mapping["mon"] = row["Mon"]
        day_machine_position_mapping["tue"] = row["Tue"]
        day_machine_position_mapping["wed"] = row["Wed"]
        day_machine_position_mapping["thu"] = row["Thu"]
        day_machine_position_mapping["fri"] = row["Fri"]
        day_machine_position_mapping["sat"] = row["Sat"]
            
        return day_machine_position_mapping
       
    def generate_schedules(self, workforce_id, start_date, end_date, day_machine_position_mapping) -> list:

        result = []

        # Convert string date to datetime object
        current_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")


        while current_date <= end_date:
            # Get the weekday name (e.g., 'Sun', 'Mon', etc.)
            weekday = current_date.strftime('%a').lower()

            # Check if the weekday exists in the dictionary
            if weekday in day_machine_position_mapping:
                defaultMachinePositionId = self.get_machine_position_mapping(day_machine_position_mapping[weekday])
                if defaultMachinePositionId is None:
                    
                    # try the next day, and skip this day schedule for given workforceId
                    current_date += timedelta(days=1)
                    continue
                
                result.append({
                    "workforceId": workforce_id,
                    "defaultMachinePositionId": defaultMachinePositionId,
                    "date": current_date.strftime("%Y-%m-%d"),

                })

            # Move to the next day
            current_date += timedelta(days=1)
        return result

        
    def set_machine_position_mapping(self) -> None:
        machine_preference_url = SHEET_API_ENDPOINTS["MachinePreference"]
        _, response = get_api(machine_preference_url)
        machine_position_mapping = {}
        for preference in response:
            source_machine_number = preference["sourceMachine"]["machineNumber"]
            target_machine_number = preference["targetMachine"]["machineNumber"]
            key = f"{source_machine_number}/{target_machine_number}"
            machine_position_mapping[key] = preference["machinePreferenceId"]
        self.machine_position_mapping = machine_position_mapping
    
    def get_machine_position_mapping(self, default_machine_position):
        if default_machine_position not in self.machine_position_mapping:
            return None
        return self.machine_position_mapping[default_machine_position]
    
    def get_final_data(self):
        self.set_machine_position_mapping()
        return self.manipulate_data()