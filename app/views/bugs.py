import os
from flask import Blueprint, render_template
from ..flask_extensions import pages

#######################################################################
# Initialize blueprint
#######################################################################
BLUEPRINT_NAME = "bugs"
bugs = Blueprint(BLUEPRINT_NAME, __name__, url_prefix="/"+BLUEPRINT_NAME)

#######################################################################
# Initialize helpers
#######################################################################
SORT_KEY = lambda i: i['date']

#######################################################################
# Handle views
#######################################################################
@bugs.route('/posts/')
def posts():
    posts = [p for p in pages if p.path.startswith(BLUEPRINT_NAME)]
    posts.sort(key=SORT_KEY, reverse=True)
    template = os.path.join(BLUEPRINT_NAME, 'posts.html')
    return render_template(template, posts=posts)

@bugs.route('/posts/<name>/')
def post(name):
    post_path = os.path.join(BLUEPRINT_NAME, name)
    post = pages.get_or_404(post_path)
    template = os.path.join(BLUEPRINT_NAME, 'post.html')
    return render_template(template, post=post)
