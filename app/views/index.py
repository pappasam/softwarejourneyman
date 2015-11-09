import os
from flask import Blueprint, render_template
from flask_flatpages import pygments_style_defs

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

@index.route('/pygments.css')
def pygments_css():
    '''View for syntax highlighting within blog posts'''
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}
