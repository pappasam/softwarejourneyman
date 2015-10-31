from flask_bootstrap import Bootstrap
from flask_flatpages import FlatPages
from flask_frozen import Freezer

######################################
# Initialize extensions
#####################################
from .navigation import nav
bootstrap = Bootstrap()
pages = FlatPages()
freezer = Freezer()

######################################
# Organize extensions
#####################################
extensions_all = [
        nav,
        bootstrap,
        pages,
        freezer,
        ]
