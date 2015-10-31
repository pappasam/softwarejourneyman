import os
from flask import Blueprint
from ..utils import blueprint_render_template_factory
from ..utils import flatpages_posts, flatpages_post

#######################################################################
# Get name of current file
#######################################################################
BLUEPRINT_NAME = __name__.split('.')[-1] # name of file

#######################################################################
# Initialize blueprint and helper functions
#######################################################################
present = Blueprint(BLUEPRINT_NAME, __name__, url_prefix='/'+BLUEPRINT_NAME)
render_template = blueprint_render_template_factory(BLUEPRINT_NAME)

#######################################################################
# Define views
#######################################################################
@present.route('/posts/')
def posts():
    posts = flatpages_posts(BLUEPRINT_NAME)
    return render_template('posts.html', posts=posts)

@present.route('/posts/<name>/')
def post(name):
    post = flatpages_post(BLUEPRINT_NAME, name)
    return render_template('post.html', post=post)
