"""
Defines the structure of email. This structure is understood by datastore layer.
"""

class email:
    def __init__(self, schedule_id , event_id , email_subject , email_content , schedule_date):
        self.schedule_id = schedule_id
        self.event_id = event_id
        self.email_subject = email_subject
        self.email_content = email_content
        self.schedule_date = schedule_date
