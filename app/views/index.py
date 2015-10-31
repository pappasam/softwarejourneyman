import os
from flask import Blueprint, render_template

#######################################################################
# Get name of current file
#######################################################################
BLUEPRINT_NAME = __name__.split('.')[-1] # name of file

#######################################################################
# Initialize blueprint and helper functions
#######################################################################
index = Blueprint(BLUEPRINT_NAME, __name__)

#######################################################################
# Define views
#######################################################################
@index.route('/')
def main_index():
    return render_template('index.html')
