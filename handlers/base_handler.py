from utils.api_caller import post_to_api

class BaseHandler:
    def __init__(self, data):
        self.data = data
    
    def manipulate_data(self):
        """Override this method in each sheet-specific handler"""
        return self.data
    
    def get_final_data(self):
        return self.manipulate_data()

    def call_additional_api(self, endpoint, data):
        """Helper method to make API calls during data manipulation"""
        status_code, response = post_to_api(data, endpoint)
        print(f"Additional API Call - Status: {status_code}, Response: {response}")
        return status_code, response
