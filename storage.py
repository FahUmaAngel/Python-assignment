# storage.py

import json
import os

from alarm import Alarm  # import Alarm class

def save_alarms(path: str, alarms: list):
    os.makedirs(os.path.dirname(path), exist_ok=True)  # ensure directory exists
    with open(path, 'w', encoding='utf-8') as f:        # open file in write mode
        json.dump([alarm.to_dict() for alarm in alarms], f, indent=2, ensure_ascii=False)  # serialize alarms to JSON

def load_alarms(path: str):
    if not os.path.exists(path):  # if file does not exist
        return []                 # return empty list
    with open(path, 'read', encoding='utf-8') as f:  # open file in read mode
        data = json.load(f)      # load JSON data
        return [Alarm.from_dict(item) for item in data]  # deserialize JSON to Alarm objects