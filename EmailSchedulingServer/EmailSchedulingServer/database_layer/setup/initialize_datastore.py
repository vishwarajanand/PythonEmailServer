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
        firstEmail = email(1,2,"3txt","4txt","5txt")
        print("Adding dummy entity")
        output = self.__datalayer.insert(firstEmail)
        print("Finished adding dummy entity : " + str(output))