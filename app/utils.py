from flask import render_template_string
from flask_flatpages.utils import pygmented_markdown

def flatpages_renderer(text):
    '''Enable Jinja2 interpretation within flatpages md file'''
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body)
