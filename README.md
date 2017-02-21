# Purpose
- Gather all eve Online data and give a convienient function to refreash your data
- all Data is static data generated with a base class as controll
- Why you are asking? Simple static code analysis makes Testing a lot easier when new features are introduced to eve api.

# goal
- make 3rd party dev for eve easier and more reliable. a package to rule them all this is python not c.
- when finished will get its own repo and will be packaged to pypi

# integration is designed for
- django with OAuth2 and a django restframework
- django middleware adds your oAuth header to EveData Request object so you dont have to think about is in Development
and have an easy to use api where only the data access of your account is the limit
- but can also be used for other frameworks just not as convient till you implement an middleware of your own

# Comfort layer
- Layer is designed to get a easy to use Access representing combination of EveData like esi and static_data

# Steps
- imports 
- Settings 
- migrate AuthUser

if you have not already
- createsuperuser 
- login_to_admin menue and an application to Django OAuth Tool Kit

now you can edit the settings for ...
and use migrateEvedata afterwards if you need to update 
the esiapi or static model, but be aware this package cant maintain future changes of eve upfront 
but we try to keep the api as stable as possible. 
And if something is realy bothering you make a pull request in git.



# Helpful Links
http://python-social-auth.readthedocs.io/en/latest/backends/eveonline.html
http://python-social-auth.readthedocs.io/en/latest/configuration/django.html