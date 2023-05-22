
import re
import pandas as pd
from typing import List

class LogParser:

    def __init__(self) -> None:

        self.log_format  = r'(?P<remote_addr>\d+\.\d+\.\d+\.\d+)\s+\S+\s+\S+\s+\[(?P<time>[^\]]+)\]\s+"(?P<request>[^"]+)"\s+(?P<status>\d+)\s+(?P<bytes_sent>\d+)\s+"(?P<referer>[^"]+)+"\s+"(?P<user_agent>(?!http)[^"]*)"'
        self.fails = []

    def search(self,regex,log_string):
        return re.search(regex,log_string)
    
    def match(self,regex,log_string):
        return re.match(regex,log_string)


    def parse_log(self,logfile_path):
        entries = []
    
        for log_string in self.read_log_file(logfile_path):
            try:
                self.result = self.search(self.log_format,log_string)
                if self.result:
                
                    ip = self.extract_ip()
                    time = self.extract_time()
                    request = self.extract_request()
                    status = self.extract_status()
                    bytes_sent = self.extract_bytes_sent()
                    referer =self.extract_referer()
                    user_agent = self.extract_user_agent()
                    entry = {
                        "ip":ip,
                        "time":time,
                        "request":request,
                        "status":status,
                        "bytes_sent":bytes_sent,
                        "referer":referer,
                        "user_agent":user_agent       
                    }
                    entries.append(entry)      
                
            except Exception as e:
                
                print("log_string==>",log_string)
                self.fails.append(log_string)
 
        return entries
    
    def read_log_file(self,logfile_path:str)->List[str]:
        contents = []
        with open(logfile_path,'r') as f:
            for line in f.readlines():
                contents.append(line)
        return contents
        
    def extract_ip(self):

        return self.result.group("remote_addr") if self.result else None

    
    def extract_time(self):

        return self.result.group("time") if self.result else None
        
    def extract_request(self):
      
        return self.result.group("request") if self.result else None
        

    def extract_status(self):

        return self.result.group("status") if self.result else None
        
    
    def extract_bytes_sent(self):

        return self.result.group("bytes_sent") if self.result else None
     
    
    def extract_referer(self):
        
        return self.result.group("referer") if self.result else None

    
    def extract_user_agent(self):
        
        return self.result.group("user_agent") if self.result else None


    def print_matches(self,match):
        for group_name,group_value in match.groupdict().items():
            print(f"{group_name}:{group_value}")

    def to_df(self,entries):
        return pd.DataFrame(entries)
    
    def failures(self):
        return self.fails

