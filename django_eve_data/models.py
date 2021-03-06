import time

import dateutil.parser
from django.contrib.auth.models import AbstractUser
from django.utils.functional import cached_property


class EveUser(AbstractUser):
    """custom User class to work with django-social-auth"""

    @cached_property
    def _eve_auth(self):
        """shortcut to python-social-auth's EVE-related extra data for this user"""
        return self.social_auth.get(provider='eveonline').extra_data

    @property
    def eve_request_header(self):
        expires_in = time.mktime(
            dateutil.parser.parse(
                self._eve_auth['expires']  # expiration time string
            ).timetuple()  # expiration timestamp
        ) - time.time()
        return {
            'access_token': self._eve_auth['access_token'],
            "token_type": "Bearer",
            'refresh_token': self._eve_auth['refresh_token'],
            # 'expires_in': expires_in,
        }

    @property
    def character_id(self):
        """get CharacterID from authentification data"""
        return self._eve_auth['id']

    def get_portrait_url(self, size=128):
        """returns URL to Character portrait from EVE Image Server"""
        return "https://image.eveonline.com/Character/{0}_{1}.jpg".format(self.character_id, size)


# 2 choices user model bei request übergeben
# Comfort moeglichkeiten
# middleware damit eine esi_instance im request schon auf einen wartet

# weiter suchen wie ich das backend vom derzeitigen nutzer bekomme

# middleware and singleton