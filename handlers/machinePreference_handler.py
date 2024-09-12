from handlers.base_handler import BaseHandler

class MachinePreferenceHandler(BaseHandler):
    def __init__(self, data, logger=None):
        super().__init__(data, logger)    
    def manipulate_data(self):
        for row in self.data:
            row["preferenceNumber"] = int(row["preferenceNumber"])
        return self.data
