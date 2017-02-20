"""
This Files creates an additional manage.py command for Django
https://docs.djangoproject.com/en/1.10/howto/custom-management-commands/
"""
from django.core.management import BaseCommand
import os
from EveData.generation.esi_builder import SwaggerAPIBuilder
from EveData.generation.static_data_builder import create_static_model


class Command(BaseCommand):
    help = 'migrates EveData, Esi-will be generated and Static Eve Data depening on your settings File'
    can_import_settings = True

    def handle(self, *args, **options):
        from django.conf import settings
        if "EVE_STATIC_DATABASE_PATH" in dir(settings):
            # migrate Eve Static Data
            # TODO irgendetwas mit rechten
            # try:
                create_static_model()
            # except Exception as error:
            #     print(error)

        if "EVE_ESI_SWAGGER_URL" in dir(settings):
            try:
                SwaggerAPIBuilder(settings.EVE_ESI_SWAGGER_URL)
            except Exception as error:
                print(error)
