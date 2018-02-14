import os
import sqlite3
import sys
from flask import (Flask, request, session, g, redirect, url_for, abort,
render_template, flash)

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py
# Load default config and override config from an environment variable
print("This is the path: " + app.root_path)
app.config.update(
	#app.root_path gets the path to the application
	DATABASE=os.path.join(app.root_path, 'flaskr.db'),
	SECRET_KEY= os.urandom(20),
	USERNAME='admin',
	PASSWORD='default'
)
#app.config.from_envvar('FLASKR_SETTINGS', silent=True) #this import settings from a seperate venv variable called FLASKR_SETTINGS
#The silent= true tells flask not to complain if the env variable "FLASKR_SETTINGS" is not set.

def connect_db():
	"""Connects to the specific database."""
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv