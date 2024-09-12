import logging

def setup_logger(request_log_file_path, response_log_file_path):
    # Configure the root logger
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Create a logger for requests
    request_logger = logging.getLogger('request_logger')
    request_handler = logging.FileHandler(request_log_file_path)
    request_handler.setFormatter(logging.Formatter('%(asctime)s - REQUEST - %(message)s'))
    request_logger.addHandler(request_handler)
    request_logger.setLevel(logging.INFO)

    # Create a logger for responses
    response_logger = logging.getLogger('response_logger')
    response_handler = logging.FileHandler(response_log_file_path)
    response_handler.setFormatter(logging.Formatter('%(asctime)s - RESPONSE - %(message)s'))
    response_logger.addHandler(response_handler)
    response_logger.setLevel(logging.INFO)

    return request_logger, response_logger