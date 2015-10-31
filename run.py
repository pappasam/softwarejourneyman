import os
import argparse
from app import create_app
from app.flask_extensions import freezer
from config import config

def command_line_parser():
    parser = argparse.ArgumentParser(description="Run flask application")
    parser.add_argument('-t', action='store', dest='config_type', type=str,
            default='default', choices=[k for k in config],
            help="Determine type of configuration parameters")
    parser.add_argument('-b', action='store_true', dest='build',
            default=False, help="Build application?")
    return parser.parse_args()

if __name__ == '__main__':
    cmdline = command_line_parser()
    application = create_app(cmdline.config_type)
    if cmdline.build:
        freezer.freeze()
    else:
        application.run()
