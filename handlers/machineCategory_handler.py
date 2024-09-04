from handlers.base_handler import BaseHandler

class MachineCategoryHandler(BaseHandler):
    def manipulate_data(self):
        for row in self.data:
            row["machineNumber"] = int(row["machineNumber"])
        return self.data
