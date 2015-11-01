import os
from flask import Blueprint
from .post_template import posts_post_init

BLUEPRINT_NAME = "tools"
tools = Blueprint(BLUEPRINT_NAME, __name__, url_prefix="/"+BLUEPRINT_NAME)
posts, post = posts_post_init(tools, BLUEPRINT_NAME)
