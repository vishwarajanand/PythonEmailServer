import sys
from datetime import datetime
import time

from database_layer.entity.email import email
from database_layer.operations.datastore_operations import datastore_operations
from email_sender.email_publisher import email_publisher
import schedule

class pull_job_scheduler:

    def __init__(self, time=10):
        self.__time = time
    
    def schedule(self):
        """
        This function schedules pull_job function.
        """
        schedule.every(self.__time).minutes.do(self.pull_job)
        while True:
            schedule.run_pending()
            time.sleep(self.__time)

    def pull_job(self):
        """
        This function pulls pending emails.
        """
        try:
            all_saved_emails = datastore_operations("").retrieve_all()
            filtered_emails = self.filter_emails(all_saved_emails)
            email_publisher().bulk_publish_email(filtered_emails)
        except Exception as ex:
            print("Exception occurred while publishing emails: " + str(ex))

    def filter_emails(self, list_emails):
        """
        This function filters emails that are required to be published in current job run.
        ToDo: Implement filtering based on date. Currently, there is no filtering.
        """
        filtered_emails = []
        for email in list_emails:
            """
            Check for email schedule time for each email.
            If scheduled time is less than current time, then email is ready for publishing.
            """
            email_scheduled_datetime = datetime.strptime(email.schedule_date, '%Y-%m-%dT%H:%M')
            time_delta = datetime.now() - email_scheduled_datetime
            if (self.__time <= time_delta.total_seconds() / 60):
                filtered_emails.append(email)

        return filtered_emails
