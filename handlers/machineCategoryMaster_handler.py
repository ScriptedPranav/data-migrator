from handlers.base_handler import BaseHandler

class MachineCategoryMasterHandler(BaseHandler):
    def __init__(self, data, logger=None):
        super().__init__(data, logger)
    def manipulate_data(self):
        return self.data
