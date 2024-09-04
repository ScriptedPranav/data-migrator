from handlers.base_handler import BaseHandler

class MachinePreferenceHandler(BaseHandler):
    def manipulate_data(self):
        for row in self.data:
            row["preferenceNumber"] = int(row["preferenceNumber"])
        return self.data
