from enum import Enum

async def execute_notify_service():
    pass

class NotificationStore:
    
    
    def __init__(self):
        self.index = 1
        notification = {}
        
    
    # class(Enum):
    #     PENDING: "pending"

    def create(self, notification_data):
        # state has this specified values
        # pending
        # delivered
        # failed
        self.index += 1
        notification_data["meta"] = {
            "state": "pending",
            "index": self.index
        }
        self.notification[self.index](notification_data)
        return self.index

    async def send(self, notification_index, sender_ids):
        for email_id in enumerate(sender_ids):
            content = self.notification[notification_index]
            execute_notify_service(content, email_id)

