"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import request, render_template
from EmailSchedulingServer import app
from database_layer.operations.datastore_operations import datastore_operations
from database_layer.entity.email import email

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template('index.html',
        title='Email Scheduler',
        year=datetime.now().year,)

@app.route('/new_schedule')
def new_schedule():
    """Renders the save new schedule page."""
    return render_template('new_schedule.html',
        title='Save New Schedule',
        year=datetime.now().year,
        message='Save New Schedule')

@app.route('/save_emails', methods=['POST'])
def save_emails():
    """Saves scheduled email to datastore."""
    try:
        print("Fetching data from UI.")
        new_email = email(request.form["event_id"],request.form["email_subject"],request.form["email_content"], str(request.form["schedule_date"]))
        print("Email data obtained, saving in datastore.")
        datastore_operations("").insert(new_email)
        print("Email data saved in datastore, redirecting user to show list of saved emails.")
        return list_schedules()
    except Exception as ex:
        print("Exception occurred while saving email schedule to datastore: " + str(ex))

@app.route('/list_schedules')
def list_schedules():
    """Fetch all saved emails"""
    saved_emails_list = datastore_operations("").retrieve_all()
    stringified_emails = [saved_email.stringify() for saved_email in saved_emails_list]
    
    """Renders the schedule list page."""
    return render_template('list_schedules.html',
        title='Saved Schedules',
        year=datetime.now().year,
        message=stringified_emails)

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html',
        title='About',
        year=datetime.now().year,
        message='This application allows users to schedule emails to be pushed at a later date.')
