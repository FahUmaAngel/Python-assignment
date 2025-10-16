# logger.py

import os
import datetime

class AppLogger:
    def __init__(self, log_dir='logs'):                 # initialize logger with log directory  
        os.makedirs(log_dir, exist_ok=True)             # ensure log directory exists
        now = datetime.datetime.now()                   # get current date and time    
        file_name = now.strftime("log_%Y%m%d_%H%M%S.txt")  # create log file name with timestamp
        self.path = os.path.join(log_dir, file_name)  # full path to log file
        
    def log(self, event: str):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")     # get current date and time
        entry = f"{now}_{event}\n"  # format log entry
        with open(self.path, 'a', encoding='utf-8') as f:   # open log file in append mode
            f.write(entry)                                  # write log entry to file