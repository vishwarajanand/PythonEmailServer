import asyncio
import sys

from database_layer.entity.email import email
from database_layer.operations.datastore_operations import datastore_operations

class email_publisher:
    
    def bulk_publish_email(self, list_emails):
        """
        Publishes emails in bulk.
        """
        if list_emails is None or len(list_emails) <= 0:
            print("No emails to publish as bulk emails.")
            return 
        for email in list_emails:
            self.publish_email(email)

    def publish_email(self, email):
        """
        Publishes email.
        """
        if email is None:
            print("No email to publish.")
            return 
        print("Publishing Email: " + str(email.schedule_id))
        self.__publishApi(email)
        print("Removing Email: " + str(email.schedule_id))
        datastore_operations("").delete(email)

    def __publishApi(self, email):
        """
        Reformats Email structure to Network API.
        """

        email_message = "Subject: " + email.email_subject + "\nContent: " + email.email_content
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.send(email_message, self.__get_to_list(), self.__get_from_list()))
        loop.close()# <-- Need to keep the event loop open for successive use.

    def __get_to_list(self):
        """
        Dummy list of recievers.
        """
        return "vishwaraj.anand00@gmail.com"

    def __get_from_list(self):
        """
        Dummy list of senders.
        """
        return "vishwaraj.anand00@gmail.com"

    async def send(self, message, to_id, from_id):
        """
        Masks Async network call to send function: ABC's magical APIs.
        ABC.messages.send(message=message, to=to, from=from, async=True)
        """
        self.__dummy_print_email(message, to_id, from_id)

    def __dummy_print_email(self, message, to_id, from_id):
        """
        Provides dummy implementation to ABC's magical APIs.
        """
        print("Email Sent: ")
        print("To: " + to_id)
        print("From: " + from_id)
        print("Message: " + message)
        print("Email Sent Successfully!")
