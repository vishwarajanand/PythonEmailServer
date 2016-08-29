"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from EmailSchedulingServer import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Email Scheduler',
        year=datetime.now().year,
    )

@app.route('/save_email')
def save_email():
    """Renders the save new schedule page."""
    return render_template(
        'save_email.html',
        title='Save New Schedule',
        year=datetime.now().year,
        message='Save New Schedule'
    )

@app.route('/list_schedules')
def list_schedules():
    """Renders the schedule list page."""
    return render_template(
        'list_schedules.html',
        title='Saved Schedules',
        year=datetime.now().year,
        message='List of all saved schedules'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='This application allows users to schedule emails to be pushed at a later date.'
    )
