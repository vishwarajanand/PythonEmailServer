"""
This script runs the EmailSchedulingServer application using a development server.
"""

from os import environ
from EmailSchedulingServer import app
from database_layer.setup.initialize_datastore import initialize_datastore
import uuid

if __name__ == '__main__':
    print("Initializing application datastore.")
    datastore_initializer = initialize_datastore(str(uuid.uuid4()))
    print("Finished initialization of application datastore.")
    
    print("Inserting dummy data.")
    datastore_initializer.initialize()
    print("Finished insertion of dummy data.")

    print("Starting server.")
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
    print("Application terminated.")
