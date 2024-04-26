from enum import Enum

async def execute_notify_service():
    pass

class NotificationStore:
    notification = {}
    index: 1
    def __init__():
        pass
    
    # class(Enum):
    #     PENDING: "pending"

        
    def create(self, notification_data):
        # state has this specified values
        # pending
        # delivered
        # failed
        index += 1
        notification_data["meta"] = {
            "state": "pending",
            "index": index
        }
        self.notification[index](notification_data)
        return index

    async def send(self, notification_index, sender_ids):
        for email_id in enumerate(sender_ids):
            content = self.notification[notification_index]
            execute_notify_service(content, email_id)

