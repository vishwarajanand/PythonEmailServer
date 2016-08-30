"""
Defines the structure of email. This structure is understood by datastore layer.
"""

class email:
    def __init__(self, event_id , email_subject , email_content , schedule_date, schedule_id = 0):
        self.schedule_id = schedule_id
        self.event_id = event_id
        self.email_subject = email_subject
        self.email_content = email_content
        self.schedule_date = schedule_date

    def stringify(self):
        string_builder = "Schedule Id: " + str(self.schedule_id) + " \n"
        string_builder += "Event Id: " + str(self.event_id) + " \n"
        string_builder += "Email Subject: " + str(self.email_subject) + " \n"
        string_builder += "Schedule Date: " + str(self.schedule_date) + " \n"
        string_builder += "Email Content: " + str(self.email_content)
        return string_builder