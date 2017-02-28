# Purpose
- Gather all eve Online data and give a convienient function to refreash your data
- all Data is static data generated with a base class as controll
- Why you are asking? Simple static code analysis makes Testing a lot easier when new features are introduced to eve api.

# Integration is designed for:
- django with OAuth2 and a django restframework
- django middleware adds your oAuth header to EveData Request object so you dont have to think about is in Development
and have an easy to use api where only the data access of your account is the limit
- but can also be used for other frameworks just not as convient till you implement an middleware of your own

# Comfort layer
- Layer is designed to get a easy to use Access representing combination of EveData like esi and static_data
- TODO 

# How to
1. pip install django_eve_data or add package to your Enviroment <br>
    # Packages you will need:
    - django
    - social-auth-app-django
    - django_eve_data

    # Optional Packages:
    - djangorestframework
    - django-cors-headers
    - django-rest-framework-social-oauth2

2. django settings full settings for OAuth2 and optional django_rest_framework:


    INSTALLED_APPS = [
        ...
        'oauth2_provider',
        'social_django',
        'django_eve_data',
        'rest_framework_social_oauth2', # Optional
        'rest_framework', # Optional
        ...
    ]
    
    MIDDLEWARE_CLASSES = [
        ...,
        'django_eve_data.middleware.EveDataMiddleware'
    ]

    TEMPLATES = [
        {   
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    # OAUTH2
                    'social_django.context_processors.backends',
                    'social_django.context_processors.login_redirect',
                ],
            },
        },
    ]
    
    # Example both are optional if you intent not to migrate new data
    EVE_STATIC_DATABASE_PATH = "Path to your static eve database " 
    EVE_ESI_SWAGGER_URL = "https://esi.tech.ccp.is/latest/swagger.json"
    
    DATABASES = {
        ...
        'eve_static_data': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': EVE_STATIC_DATABASE_PATH,
        }
    }
    
    AUTHENTICATION_BACKENDS = (
        # Eve Backend
        'social_core.backends.eveonline.EVEOnlineOAuth2',
        # OAuth2 backend
        'rest_framework_social_oauth2.backends.DjangoOAuth2',
        'django.contrib.auth.backends.ModelBackend',
    )

    LOGIN_URL = '/login/'
    LOGIN_REDIRECT_URL = '/'
    SOCIAL_AUTH_EVEONLINE_KEY = 'enter your key from eve online' 
    SOCIAL_AUTH_EVEONLINE_SECRET = 'enter your secret from eve online'
    SOCIAL_AUTH_CLEAN_USERNAMES = False
    # Comment out or delete the rights you dont need
    SOCIAL_AUTH_EVEONLINE_SCOPE = [
        'publicData',
        'remoteClientUI',
        'esi-calendar.respond_calendar_events.v1',
        'esi-calendar.read_calendar_events.v1',
        'esi-location.read_location.v1',
        'esi-location.read_ship_type.v1',
        'esi-mail.organize_mail.v1',
        'esi-mail.read_mail.v1',
        'esi-mail.send_mail.v1',
        'esi-skills.read_skills.v1',
        'esi-skills.read_skillqueue.v1',
        'esi-wallet.read_character_wallet.v1',
        'esi-search.search_structures.v1',
        'esi-clones.read_clones.v1',
        'esi-characters.read_contacts.v1',
        'esi-universe.read_structures.v1',
        'esi-bookmarks.read_character_bookmarks.v1',
        'esi-killmails.read_killmails.v1',
        'esi-corporations.read_corporation_membership.v1',
        'esi-assets.read_assets.v1',
        'esi-planets.manage_planets.v1',
        'esi-fleets.read_fleet.v1',
        'esi-fleets.write_fleet.v1',
        'esi-ui.open_window.v1',
        'esi-ui.write_waypoint.v1',
        'esi-characters.write_contacts.v1',
        'esi-fittings.read_fittings.v1',
        'esi-fittings.write_fittings.v1',
        'esi-markets.structure_markets.v1'
    ]
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'oauth2_provider.ext.rest_framework.OAuth2Authentication',
            'rest_framework_social_oauth2.authentication.SocialAuthentication',
            'rest_framework.authentication.SessionAuthentication',
        ),
    }
    AUTH_USER_MODEL = 'django_eve_data.EveUser'
    

# Migrate eve_data 
If you want newer data then the package provides you can migrate new static_db_model 
and python esi_api yourself. But be aware its not testet dont write silly issues without mentioning it!
1.  open a console where your manage.py is 
2.  python manage.py -h <br>
    This command should give you the option migrate_eve_data
3.  execute: python manage.py migrate_eve_data

# Setting up your Social Auth also explained in the links below
if you have not already
- createsuperuser 
- login to your adminmenue and add am application to Django OAuth Tool Kit

# Useage
basic esi useage (Charakter and so on only work after middleware is executed or header is set manualy)

    from django_eve_data.esi_api import alliances
    print(alliances.Alliances().get())
    
or comfort layer in future
    
    from django_eve_data.comfort_layer import *
    
or for static data model

    from django_eve_data.static_data_export.static_model import *
    

# Helpful Links if i missed smth in oAuth2 or restframework
http://python-social-auth.readthedocs.io/en/latest/backends/eveonline.html
http://python-social-auth.readthedocs.io/en/latest/configuration/django.html

#
If you want to help make an issue or better a pull request with a solution. 
There should be plenty comfort classes missing you can add
