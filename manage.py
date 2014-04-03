#!/usr/bin/env python

import os
import sys


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)


# Add the site ID CLI arg to the environment, which allows for the site
# used in any site related queries to be manually set for management
# commands.
for i, arg in enumerate(sys.argv):
    if arg.startswith("--site"):
        os.environ["MEZZANINE_SITE_ID"] = arg.split("=")[1]
        sys.argv.pop(i)


# Run Django.
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
