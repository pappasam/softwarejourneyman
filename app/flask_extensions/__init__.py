from flask_bootstrap import Bootstrap
from flask_flatpages import FlatPages

######################################
# Initialize extensions
#####################################
from .navigation import nav
bootstrap = Bootstrap()
pages = FlatPages()

######################################
# Organize extensions
#####################################
extensions_all = [
        nav,
        bootstrap,
        pages,
        ]
