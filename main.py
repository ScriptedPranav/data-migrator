import os
from utils.excel_reader import read_excel
from utils.api_caller import post_to_api
from mappings.column_mappings import COLUMN_MAPPINGS
from mappings.sheet_handlers import SHEET_HANDLERS
from mappings.sheet_api_endpoints import SHEET_API_ENDPOINTS


def main(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        exit(1)
        
    for sheet_name, column_mapping in COLUMN_MAPPINGS.items():
        handler_class = SHEET_HANDLERS.get(sheet_name)
        
        if handler_class is None:
            print(f"No handler found for {sheet_name}, skipping...")
            continue
        
        sheet_api_endpoint = SHEET_API_ENDPOINTS.get(sheet_name)
        if sheet_api_endpoint is None:
            print("No url found for", sheet_name)
            continue

        data_list = read_excel(file_path, sheet_name, column_mapping)
        
        # Instantiate the handler for the current sheet
        handler = handler_class(data_list)
        final_data_list = handler.get_final_data()

        
        for data in final_data_list:
            status_code, response = post_to_api(data, sheet_api_endpoint)
            print(f"Status: {status_code}, Response: {response}")

if __name__ == "__main__":
    main("data/Production AutoCrew Master Data.xlsx")
