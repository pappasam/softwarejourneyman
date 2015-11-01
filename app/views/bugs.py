import os
from flask import Blueprint
from .post_template import posts_post_init

BLUEPRINT_NAME = "bugs"
bugs = Blueprint(BLUEPRINT_NAME, __name__, url_prefix="/"+BLUEPRINT_NAME)
posts, post = posts_post_init(error, BLUEPRINT_NAME)
