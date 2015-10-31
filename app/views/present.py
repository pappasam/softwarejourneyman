import os
from flask import Blueprint
from ..flask_extensions import pages
from ..utils import blueprint_render_template_factory

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
    posts = [p for p in pages if p.path.startswith(BLUEPRINT_NAME)]
    posts.sort(key=lambda item:item['date'], reverse=True)
    return render_template('posts.html', posts=posts)

@present.route('/posts/<name>/')
def post(name):
    post_path = os.path.join(BLUEPRINT_NAME, name)
    post = pages.get_or_404(post_path)
    return render_template('post.html', post=post)
