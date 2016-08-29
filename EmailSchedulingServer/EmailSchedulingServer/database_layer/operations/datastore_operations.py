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
            tableQuery = """INSERT INTO scheduled_emails (schedule_id , event_id , email_subject , email_content , schedule_date) VALUES 
                            (""" + str(email.schedule_id) + "," + str(email.event_id) + ",'" + email.email_subject + "','" + email.email_content + "','" + email.schedule_date + """') 
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
                            SET event_id=""" + email.event_id + ", email_subject='" + email.email_subject + "',email_content='" + email.email_content + "', schedule_date='" + email.schedule_date + """'
                            WHERE schedule_id=""" + email.schedule_id
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
            tableQuery = """DELETE FROM scheduled_emails WHERE schedule_id=""" + email.schedule_id
            print("Trying to delete entity.")
            rows_affected = dbLink.execute(tableQuery)
            print("Entity deletion finished.")
            dbConnection.commit()
            dbConnection.close()
            return rows_affected
        except Exception as ex:
            print("Exception occurred while deleting entity from datastore: " + str(ex))
            return str(ex)
    
    # Searches and retrieves entities from Datastore.
    def search(self, email):
        try:
            print("Connecting to DB.")
            dbConnection = sqlite3.connect(self.__db_name)
            dbLink = dbConnection.cursor()
            print("DB connection link established.")
            tableQuery = """SELECT schedule_id , event_id , email_subject , email_content , schedule_date FROM scheduled_emails 
                            WHERE schedule_id=""" + email.schedule_id
            print("Trying to search entity.")
            rows_affected = dbLink.execute(tableQuery)
            print("Entity retrieval finished.")
            result = dbLink.fetchone()
            fetched_email = email(result[0], result[1], result[2], result[3], result[4]);
            dbConnection.commit()
            dbConnection.close()
            return fetched_email
        except Exception as ex:
            print("Exception occurred while retrieving entity from datastore: " + str(ex))
            return str(ex)
