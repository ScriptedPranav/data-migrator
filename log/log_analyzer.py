import os
from datetime import datetime
import re

class LogAnalyzer:
    def __init__(self, log_file_path):
        if not os.path.exists(log_file_path):
            raise FileNotFoundError(f"File not found: {log_file_path}")
        
        with open(log_file_path, 'r') as file:
            self.log_lines = file.readlines()

        self.time_format = "%Y-%m-%d %H:%M:%S,%f"
    
    def _extract_timestamp(self, log_line):
        return datetime.strptime(log_line[:23], self.time_format)

    def _filter_logs_by_sheet(self, sheet_name):
        """Filter log lines that contain the specified sheet name."""
        return [line for line in self.log_lines if f'Sheet : {sheet_name}' in line]
    
    def get_total_time_elapsed(self):
        """Calculate total time from first to last log, without filtering by sheet."""
        if not self.log_lines:
            return 0
        first_log_time = self._extract_timestamp(self.log_lines[0])
        last_log_time = self._extract_timestamp(self.log_lines[-1])
        return (last_log_time - first_log_time).total_seconds()

    def get_total_time_elapsed_for_sheet(self, sheet_name):
        """Calculate total time from first to last log for a specific sheet."""
        filtered_logs = self._filter_logs_by_sheet(sheet_name)
        if not filtered_logs:
            return 0
        first_log_time = self._extract_timestamp(filtered_logs[0])
        last_log_time = self._extract_timestamp(filtered_logs[-1])
        return (last_log_time - first_log_time).total_seconds()

    def search_logs(self, sheet_name, status_code=None, request_id=None, date=None):
        """
        Search logs with complex filtering criteria based on sheet name,
        status code, request ID, or date.
        """
        filtered_logs = self._filter_logs_by_sheet(sheet_name)

        if status_code:
            filtered_logs = [line for line in filtered_logs if f'Status Code: {status_code}' in line]
        
        if request_id:
            filtered_logs = [line for line in filtered_logs if f'Request ID: {request_id}' in line]

        if date:
            date_pattern = re.compile(r"date': '(\d{4}-\d{2}-\d{2})'")
            filtered_logs = [line for line in filtered_logs if date_pattern.search(line) and date in line]

        return filtered_logs

    def get_log_summary(self, sheet_name=None):
        """Return a summary of logs for a sheet or overall, including count of status codes."""
        logs_to_summarize = self._filter_logs_by_sheet(sheet_name) if sheet_name else self.log_lines
        
        status_code_count = {}
        status_code_pattern = re.compile(r"Status Code: (\d{3})")
        
        for log_line in logs_to_summarize:
            match = status_code_pattern.search(log_line)
            if match:
                status_code = match.group(1)
                status_code_count[status_code] = status_code_count.get(status_code, 0) + 1
        
        return status_code_count

    def get_corresponding_logs_from_requests(self, responses_log_file, requests_log_file, sheet_name, status_code, date=None):
        """
        Given sheet_name, status_code, and optional date from responses.log,
        this method finds all corresponding request IDs and retrieves matching logs from requests.log.
        """
        # Read responses log
        if not os.path.exists(responses_log_file):
            raise FileNotFoundError(f"File not found: {responses_log_file}")
        with open(responses_log_file, 'r') as file:
            responses_logs = file.readlines()

        # Search responses log for matching request IDs
        matching_responses = self.search_logs(sheet_name, status_code=status_code, date=date)
        request_ids = []
        request_id_pattern = re.compile(r"Request ID: ([\w-]+)")

        for log in matching_responses:
            match = request_id_pattern.search(log)
            if match:
                request_ids.append(match.group(1))

        # Read requests log
        if not os.path.exists(requests_log_file):
            raise FileNotFoundError(f"File not found: {requests_log_file}")
        with open(requests_log_file, 'r') as file:
            requests_logs = file.readlines()

        # Find corresponding logs in requests.log based on the extracted request IDs
        matching_requests = []
        for log in requests_logs:
            if any(request_id in log for request_id in request_ids):
                matching_requests.append(log)

        return matching_requests



log_analyzer = LogAnalyzer("log/responses.log")
result = log_analyzer.get_corresponding_logs_from_requests("log/responses.log", "log/requests.log","Combined", 400)
for log in result:
    print(log)