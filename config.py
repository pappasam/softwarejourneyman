import os
from app.utils import flatpages_renderer

basedir = os.path.abspath(os.path.dirname(__file__))

class ConfigBase(object):
    SECRET_KEY = os.urandom(24)

    FLATPAGES_ROOT = "./content/"
    FLATPAGES_EXTENSION = '.md'
    FLATPAGES_HTML_RENDERER = flatpages_renderer

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(ConfigBase):
    DEBUG = True
    FLATPAGES_AUTORELOAD = True

class DeploymentConfig(ConfigBase):
    DEBUG = False
    FLATPAGES_AUTORELOAD = False

config = {
        'development': DevelopmentConfig,
        'deployment': DeploymentConfig,
        'default': DevelopmentConfig,
        }
