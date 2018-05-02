#!/usr/bin/env python
import os
import sys
import dotenv

ENV_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #; print(ENV_DIR)

if __name__ == "__main__":
    try:
        dotenv.read_dotenv(os.path.join(ENV_DIR, '.env'))
        print('Reading environmental variables from .env')
    except Exception as exc:
        print('Local .env file not found:' + exc)
        
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dmlgeodjango.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
