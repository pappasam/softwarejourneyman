import os
from flask import render_template, render_template_string
from flask_flatpages.utils import pygmented_markdown
from typing import Callable

def blueprint_render_template_factory(subdirectory: str) -> Callable:
    '''Return function to render templates in given subdirectory

    :param subdirectory: subdirectory of blueprint templates
    '''
    def f(filename, **kwargs):
        full_file = os.path.join(subdirectory, filename)
        return render_template(full_file, **kwargs)
    return f

def flatpages_renderer(text):
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body)
