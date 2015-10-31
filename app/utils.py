import os
from flask import render_template, render_template_string
from flask_flatpages.utils import pygmented_markdown

from .flask_extensions import pages

def blueprint_render_template_factory(subdirectory):
    '''Return function to render templates in given subdirectory

    :param subdirectory: subdirectory of blueprint templates
    '''
    def f(filename, **kwargs):
        full_file = os.path.join(subdirectory, filename)
        return render_template(full_file, **kwargs)
    return f

def flatpages_renderer(text):
    '''Enable Jinja2 interpretation within flatpages md file'''
    prerendered_body = render_template_string(text)
    return pygmented_markdown(prerendered_body)

def flatpages_posts(blueprint_name, sort_val='date'):
    '''Return sorted posts from blueprint name

    :param blueprint_name: value of blueprint
    :param sort_val: name of yaml configuration by which to sort
    '''
    posts = [p for p in pages if p.path.startswith(blueprint_name)]
    posts.sort(key=lambda item:item[sort_val], reverse=True)
    return [i for i in posts]

def flatpages_post(blueprint_name, post_name):
    '''Return content from specific post name from blueprint'''
    post_path = os.path.join(blueprint_name, post_name)
    return pages.get_or_404(post_path)
