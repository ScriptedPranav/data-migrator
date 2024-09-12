import os
import uuid

from utils.excel_reader import read_excel
from utils.api_caller import post_api
from utils.logger import setup_logger

from mappings.column_mappings import COLUMN_MAPPINGS
from mappings.sheet_handlers import SHEET_HANDLERS
from mappings.sheet_api_endpoints import SHEET_API_ENDPOINTS


def main(data_file_path, request_log_file_path, response_log_file_path):
    if not os.path.exists(data_file_path):
        print(f"File not found: {data_file_path}")
        exit(1)
        
    # Setup the loggers
    request_logger, response_logger = setup_logger(request_log_file_path, response_log_file_path)

    for sheet_name, column_mapping in COLUMN_MAPPINGS.items():
        handler_class = SHEET_HANDLERS.get(sheet_name)
        
        if handler_class is None:
            print(f"No handler found for {sheet_name}, skipping...")
            continue
        
        sheet_api_endpoint = SHEET_API_ENDPOINTS.get(sheet_name)
        if sheet_api_endpoint is None:
            print(f"No URL found for {sheet_name}, skipping...")
            continue

        data_list = read_excel(data_file_path, sheet_name, column_mapping)
        

        # Handlers need request_logger
        handler = handler_class(data_list, request_logger)
        final_data_list = handler.get_final_data()

        for data in final_data_list:
            # Assign a unique ID for tracing this request
            request_id = str(uuid.uuid4())

            # Log the request with the unique ID
            request_logger.info(f"Request ID: {request_id} - Data: {data}")
            
            # Post the data and capture the response
            status_code, response = post_api(data, sheet_api_endpoint)
            
            # Log the response based on the status code
            if 200 <= status_code < 300:
                response_logger.info(f"Request ID: {request_id} - Status Code: {status_code}, Response: {response}")
            else:
                response_logger.error(f"Request ID: {request_id} - Status Code: {status_code}, Response: {response}")
            


if __name__ == "__main__":
    main("data/machine_schedule.xlsx", "log/requests.log", "log/responses.log")
