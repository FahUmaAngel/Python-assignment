# alarm.py
import time
import uuid

class Alarm:
    
    def __init__(self, metric: str, threshold: int, id: str = None, created_at: float = None):      # initialize Alarm object
        self.id = id or str(uuid.uuid4())               # unique identifier for the alarm
        self.metric = metric                             # metric to monitor (CPU, Memory, Disk)
        self.threshold = int(threshold)                       # threshold value for the alarm
        self.created_at = created_at or time.time()     # timestamp when the alarm was created
    
    def to_dict(self):                                  # convert Alarm object to dictionary
        return {
            'id': self.id,
            'metric': self.metric,
            'threshold': self.threshold,
            'created_at': self.created_at
        }
        
    @staticmethod
    def from_dict(data):                        # create Alarm object from dictionary
        return Alarm(                           # return new Alarm instance
            id = data.get("id"),                # get id from data, default to None if not present
            metric = data["metric"],            # get metric from data
            threshold = data["threshold"],      # get threshold from data
            created_at = data["created_at"]     # get created_at from data
        )