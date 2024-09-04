from handlers.base_handler import BaseHandler

class RoleCategoryMasterHandler(BaseHandler):
    def manipulate_data(self):
        # for row in self.data:
            # # Example manipulation: Add a new key-value pair
            # row["new_key"] = row["json_key_1"] * 2  # Assuming json_key_1 is numeric
            
            # # Example of making an additional API call
            # additional_data = {"key": row["json_key_1"]}
            # self.call_additional_api("https://example.com/another-endpoint", additional_data)
        
        return self.data
