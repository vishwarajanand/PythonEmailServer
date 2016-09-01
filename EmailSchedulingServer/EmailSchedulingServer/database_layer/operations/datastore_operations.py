"""
Defines functions to access datastore layer.
"""

import sqlite3
from database_layer.setup.datastore import datastore
from database_layer.entity.email import email

class datastore_operations:
    
    def __init__(self, db_name):
        self.__db_name = datastore(db_name).get_db_name()

    # Inserts entity into Datastore.
    def insert(self, email):
        try:
            print("Connecting to DB.")
            dbConnection = sqlite3.connect(self.__db_name)
            dbLink = dbConnection.cursor()
            print("DB connection link established.")
            tableQuery = """INSERT INTO scheduled_emails (event_id , email_subject , email_content , schedule_date) VALUES 
                            (""" + str(email.event_id) + ",'" + email.email_subject + "','" + email.email_content + "','" + email.schedule_date + """') 
                         """
            print("Trying to insert entity.")
            rows_affected = dbLink.execute(tableQuery)
            print("Entity insertion finished.")
            dbConnection.commit()
            dbConnection.close()
            return rows_affected
        except Exception as ex:
            print("Exception occurred while inserting entity in datastore: " + str(ex))
            return str(ex)
    
    # Updates entity into Datastore.
    def update(self, email):
        try:
            print("Connecting to DB.")
            dbConnection = sqlite3.connect(self.__db_name)
            dbLink = dbConnection.cursor()
            print("DB connection link established.")
            tableQuery = """UPDATE FROM scheduled_emails 
                            SET event_id=""" + str(email.event_id) + ", email_subject='" + email.email_subject + "',email_content='" + email.email_content + "', schedule_date='" + email.schedule_date + """'
                            WHERE schedule_id=""" + str(email.schedule_id)
            print("Trying to update entity.")
            rows_affected = dbLink.execute(tableQuery)
            print("Entity updation finished.")
            dbConnection.commit()
            dbConnection.close()
            return rows_affected
        except Exception as ex:
            print("Exception occurred while updating entity in datastore: " + str(ex))
            return str(ex)
    
    # Deletes entities from Datastore.
    def delete(self, email):
        try:
            print("Connecting to DB.")
            dbConnection = sqlite3.connect(self.__db_name)
            dbLink = dbConnection.cursor()
            print("DB connection link established.")
            tableQuery = """DELETE FROM scheduled_emails WHERE schedule_id=""" + str(email.schedule_id)
            print("Trying to delete entity.")
            rows_affected = dbLink.execute(tableQuery)
            print("Entity deletion finished.")
            dbConnection.commit()
            dbConnection.close()
            return rows_affected
        except Exception as ex:
            print("Exception occurred while deleting entity from datastore: " + str(ex))
            return str(ex)
    
    # Retrieves entities from Datastore.
    def retrieve_all(self):
        try:
            print("Connecting to DB.")
            dbConnection = sqlite3.connect(self.__db_name)
            dbLink = dbConnection.cursor()
            print("DB connection link established.")
            tableQuery = """SELECT event_id , email_subject , email_content , schedule_date , schedule_id FROM scheduled_emails"""

            print("Trying to search entity.")
            rows_affected = dbLink.execute(tableQuery)
            print("Entity retrieval finished.")
            result_rows = dbLink.fetchall()

            print("Parsing retrieved data.")
            fetched_emails = [email(result_row[0], result_row[1], result_row[2], result_row[3], result_row[4]) for result_row in result_rows]
            print("Finished parsing data.")
            dbConnection.commit()
            dbConnection.close()
            return fetched_emails
        except Exception as ex:
            print("Exception occurred while retrieving entity from datastore: " + str(ex))
            return str(ex)
