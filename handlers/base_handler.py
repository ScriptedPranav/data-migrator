class BaseHandler:
    def __init__(self, data, logger=None):
        self.data = data
        self.logger = logger
    
    def manipulate_data(self):
        """Override this method in each sheet-specific handler"""
        return self.data
    
    def get_final_data(self):
        return self.manipulate_data()

    def call_additional_api(self, endpoint, data):
        raise NotImplementedError()
