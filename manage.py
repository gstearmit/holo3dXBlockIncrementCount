"""Manage.py file for XBlock"""
import os
import sys

import django
#from django.core import context_processors

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workbench.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
