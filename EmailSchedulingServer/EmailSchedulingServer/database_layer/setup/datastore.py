"""
Initializes the databases for datastore layer.
"""

import sqlite3

class datastore:
    __instance = None
    __initialized = False
    
    # Overrides new behavior for creating a singleton class of datastore
    def __new__(cls, *args, **kwargs):
        # create instance if never inatantiated
        if not cls.__instance:
            cls.__instance = super(datastore, cls).__new__(cls)
        return cls.__instance

    def __init__(self, db_name):
        # Setup tables if datastore if not done
        if not self.__initialized:
            self.__db_name = db_name
            print("Creating tables in datastore for supporting data operations.")
            self.__create_datastore()
            print("Finished creating tables in datastore.")

#    @staticmethod
    def __create_datastore(self):
        try:
            print("Connecting to DB.")
            DbConnection = sqlite3.connect(self.__db_name)
            DbLink = DbConnection.cursor()
            print("DB connection link established.")
            createTableQuery = """CREATE TABLE scheduled_emails
                                   (schedule_id INTEGER PRIMARY KEY, event_id INTEGER, email_subject TEXT, email_content TEXT, schedule_date TEXT) 
                                """
            print("Trying to create tables.")
            DbLink.execute(createTableQuery)
            print("Table creation finished.")
            DbConnection.commit()
            DbConnection.close()
            self.__initialized = True
        except Exception as ex:
            print("Exception occurred while creating tables in datastore: " + str(ex))

    def get_db_name(self):
       return self.__db_name
