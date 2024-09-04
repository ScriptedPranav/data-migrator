from handlers.base_handler import BaseHandler

class WorkforceDataOverviewHandler(BaseHandler):
    def manipulate_data(self):
        for row in self.data:
            print(row)
        return self.data
