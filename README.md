## Log Parser

The Log Parser is a Python class that allows you to parse log files based on a specified log format. It extracts relevant log entries from a log file and provides methods to retrieve specific fields from the log entries.

**Features**

 - Parse log files based on a specified log format
   
 - Extract IP addresses, timestamps, request details, response statuses,bytes sent, referer URLs, and user agents from log entries
 - Generate a Pandas DataFrame from the parsed log entries
 - Keep track of any log entries that failed to parse


**Requirements**

   - Python 3.x
 - re (regular expression) module
 - pandas library
 
**Usage**

    pip install -r requirements.txt


## Instantiate the LogParser class:

    log_parser = LogParser()

Parse a log file by calling the parse_log method and providing the path to the log file as an argument. This method returns a list of dictionaries, where each dictionary represents a parsed log entry.

    entries = log_parser.parse_log(logfile_path)

Extract specific fields from the log entries using the provided methods, such as extract_ip, extract_time, extract_request, extract_status, extract_bytes_sent, extract_referer, and extract_user_agent.

    ip = log_parser.extract_ip()
    time = log_parser.extract_time()
    request = log_parser.extract_request()
    status = log_parser.extract_status()
    bytes_sent = log_parser.extract_bytes_sent()
    referer = log_parser.extract_referer()
    user_agent = log_parser.extract_user_agent()

  Generate a Pandas DataFrame from the parsed log entries using the to_df method.

      df = log_parser.to_df(entries)


Additional Notes

The log file can be read using the read_log_file method, which returns the contents of the log file as a list of strings.

The print_matches method can be used to display the matched fields and their values from a log entry.

Feel free to customize the code and adapt it to your specific use case. Happy log parsing!

