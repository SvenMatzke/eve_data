import json

import pycrest
from django.conf import settings


class FleetCrestCommands(object):
    def __init__(self, request, fleet_url):
        self.authed_crest = pycrest.eve.AuthedConnection(
            res=request.user._get_crest_tokens(),
            endpoint='https://crest-tq.eveonline.com',
            oauth_endpoint=pycrest.EVE()._oauth_endpoint,
            client_id=settings.SOCIAL_AUTH_EVEONLINE_KEY,
            api_key=settings.SOCIAL_AUTH_EVEONLINE_SECRET
        )
        self._fleet_url = fleet_url

    def refresh(self):
        self.authed_crest.refresh()

    def create_new_wing(self, fleet_url):
        url = "{0}wings/".format(fleet_url)
        return self.authed_crest.post(url)

    def create_new_squad(self, wing_id): # wing_id optional
        url = "{0}squads/".format(wing_url)
        return self.authed_crest.post(url)

    def get_fleet_structure(self):
        """
        :return: structure of crest.interfaces.ts
        """
        self.authed_crest.refresh()
        url = "{0}wings/".format(self._fleet_url)
        fleet = dict()
        fleet['wings'] = list()
        for wing in self.authed_crest.get(url).get('items'):
            new_wing = dict()
            new_wing['squads'] = list()
            new_wing['id'] = wing.get('id')
            new_wing['name'] = wing.get('name')
            for squad in wing.get('squadsList', []):
                new_squad = dict()
                new_squad['id'] = squad.get('id')
                new_squad['name'] = squad.get('name')
                new_wing['squads'].append(new_squad)
            fleet['wings'].append(new_wing)
        return fleet

    def get_fleet_member(self):
        self.authed_crest.refresh()
        url = "{0}members/".format(self._fleet_url)
        memberlist = list()
        for member in self.authed_crest.get(url).get('items'):
            new_member = dict()
            new_member['wing_id'] = member.get('wingID', -1)
            new_member['squad_id'] = member.get('squadID', -1)
            new_member['ship'] = {
                "id": member.get('ship').get('id'),
                "name": member.get('ship').get('name')
            }
            new_member['takesFleetWarp'] = member.get('takesFleetWarp', True)
            new_member['role'] = member.get('roleName')  # default member
            new_member['solarSystem'] = {
                "id": member.get('solarSystem').get('id'),
                "name": member.get('solarSystem').get('name')
            }
            new_member['character'] = {
                "id": member.get('character').get('id'),
                "name": member.get('character').get('name')
            }
            memberlist.append(new_member)
        return memberlist

    # def get_fleet_members(self, fleet_url):
    #     retr2 = {'pageCount': 1, 'pageCount_str': '1', 'totalCount': 1,
    #              'items': [{'joinTime': '2016-08-30T18:01:36',
    #                         'ship': {'name': 'Malediction',
    #                                  'id_str': '11186',
    #                                  'id': 11186,
    #                                  'href': 'https://crest-tq.eveonline.com/inventory/types/11186/'},
    #                         'takesFleetWarp': True,
    #                         'squadID': -1, 'squadID_str': '-1',
    #                         'roleID': 1, 'boosterID_str': '1',
    #                         'href': 'https://crest-tq.eveonline.com/fleets/1054411260314/members/94015645/',
    #                         'character': {
    #                             'name': 'Haucher Nactar',
    #                             'id_str': '94015645',
    #                             'id': 94015645,
    #                             'href': 'https://crest-tq.eveonline.com/characters/94015645/',
    #                             'isNPC': False},
    #                         'roleID_str': '1',
    #                         'wingID_str': '-1',
    #                         'boosterName': 'Fleet Booster',
    #                         'roleName': 'Fleet Commander (Boss)',
    #                         'solarSystem': {'name': 'Litom',
    #                                         'id_str': '30001048',
    #                                         'id': 30001048,
    #                                         'href': 'https://crest-tq.eveonline.com/solarsystems/30001048/'},
    #                         'wingID': -1, 'station': {
    #                      'name': 'Litom XI - Moon 2 - Guardian Angels Assembly Plant', 'id_str': '60012904',
    #                      'id': 60012904,
    #                      'href': 'https://crest-tq.eveonline.com/stations/60012904/'}, 'boosterID': 1}],
    #              'totalCount_str': '1'}
    #     lastretr = {'takesFleetWarp': True, 'wingID': 2097211259778,
    #                 'href': 'https://crest-tq.eveonline.com/fleets/1083011259778/members/94015645/', 'roleID': 3,
    #                 'solarSystem': {'name': 'A-ELE2', 'id_str': '30004708',
    #                                 'href': 'https://crest-tq.eveonline.com/solarsystems/30004708/', 'id': 30004708},
    #                 'character': {'href': 'https://crest-tq.eveonline.com/characters/94015645/', 'id_str': '94015645',
    #                               'isNPC': False,
    #                               'name': 'Haucher Nactar', 'id': 94015645},
    #                 'station': {'name': 'A-ELE2 VI - Blood Raiders Assembly Plant', 'id_str': '60014944',
    #                             'href': 'https://crest-tq.eveonline.com/stations/60014944/', 'id': 60014944},
    #                 'joinTime': '2016-08-28T17:31:00',
    #                 'squadID': 3157711259778,
    #                 'roleName': 'Squad Commander (Boss)',
    #                 'boosterID': 3,
    #                 'roleID_str': '3', 'boosterName': 'Squad Booster',
    #                 'ship': {'name': 'Malediction', 'id_str': '11186',
    #                          'href': 'https://crest-tq.eveonline.com/inventory/types/11186/',
    #                          'id': 11186}, 'boosterID_str': '3', 'squadID_str': '3157711259778',
    #                 'wingID_str': '2097211259778'}
    #     url = "{0}members/".format(fleet_url)
    #     val = self.authed_crest.get(url)
    #     return val

    def kick_member(self, member_url):
        self.authed_crest.delete(member_url)
        return 0

    def move_member(self, member_url, newWingId, newSquadId, newRole):
        data = {'newSquadID': newSquadId,
                'newWingID': newWingId,
                'newRole': newRole,
                }
        self.authed_crest.put(member_url, json.dumps(data))
        return

    def rename(self, url, name):# wingId squadid
        data = {'name': name}
        self.authed_crest.put(url, json.dumps(data))
        return

    def remove_squad(self, squad_url):# wingId squadid optional
        self.authed_crest.delete(squad_url)
        return

    def remove_wing(self, wing_url):
        self.authed_crest.delete(wing_url)
        return