from database_layer.entity.email import email
import sqlite3
from database_layer.operations.datastore_operations import datastore_operations
import os
import sys

class initialize_datastore:
    
    def __init__(self, db_name):
        self.__datalayer = datastore_operations(db_name)

    def initialize(self):
        print("Creating dummy entity")
        firstEmail = email(0,"dummy_email_subject","dummy_email_content", "0001-01-01T00:00")
        print("Adding dummy entity")
        output = self.__datalayer.insert(firstEmail)
        print("Finished adding dummy entity : " + str(output))
