"""
This script runs the EmailSchedulingServer application using a development server.
"""

import threading
import uuid

from database_layer.setup.initialize_datastore import initialize_datastore
from email_sender.pull_job_scheduler import pull_job_scheduler
from EmailSchedulingServer import app
from os import environ

if __name__ == '__main__':
    print("Initializing application datastore.")
    datastore_initializer = initialize_datastore(str(uuid.uuid4()))
    print("Finished initialization of application datastore.")
    
    print("Inserting dummy data.")
    datastore_initializer.initialize()
    print("Finished insertion of dummy data.")

    print("Starting email publisher job.")
    email_publisher_job = pull_job_scheduler()
    threading.Thread(target=email_publisher_job.schedule).start()
    print("Email publisher job is up and running.")

    print("Starting server.")
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
    print("Application terminated.")
