"""
https://docs.djangoproject.com/en/dev/ref/django-admin/#inspectdb

The meaning is to load a sqlite table and create the static model for django with django
"""
from django.core.management.commands import inspectdb
import os


def create_static_model():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    new_command = inspectdb.Command()
    retr = new_command.handle_inspection(
        {
            'table': None,
            'database': 'eve_static_data'
        }
    )
    static_model_path = os.path.join(os.path.dirname(current_dir), 'static_data_export', 'static_model.py')
    with open(static_model_path, 'w+') as static_model_file:
        static_model_file.write("\n".join(list(retr)))
