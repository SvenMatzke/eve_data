# coding utf-8
"""
Autogenerated Template File
"""

from .base import EsiRequestObject


class FleetsDetailWings(object):
    base_url = "https://esi.tech.ccp.is/latest/fleets/{fleet_id}/wings/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_fleets_fleet_id_wings_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_fleets_fleet_id_wings_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'get_fleets_fleet_id_wings_403_forbidden'}}, 'description': 'Forbidden', 'title': 'get_fleets_fleet_id_wings_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.read_fleet.v1'}}, 'description': 'Forbidden'}, '200': {'schema': {'items': {'title': 'get_fleets_fleet_id_wings_200_ok', 'type': 'object', 'properties': {'squads': {'items': {'title': 'get_fleets_fleet_id_wings_squad', 'type': 'object', 'properties': {'id': {'format': 'int64', 'type': 'integer', 'description': 'id integer', 'title': 'get_fleets_fleet_id_wings_id'}, 'name': {'type': 'string', 'description': 'name string', 'title': 'get_fleets_fleet_id_wings_name'}}, 'description': 'squad object', 'required': ['name', 'id']}, 'type': 'array', 'description': 'squads array', 'title': 'get_fleets_fleet_id_wings_squads'}, 'id': {'format': 'int64', 'type': 'integer', 'description': 'id integer', 'title': 'get_fleets_fleet_id_wings_id'}, 'name': {'type': 'string', 'description': 'name string', 'title': 'get_fleets_fleet_id_wings_name'}}, 'description': '200 ok object', 'required': ['name', 'id', 'squads']}, 'type': 'array', 'description': '200 ok array', 'title': 'get_fleets_fleet_id_wings_ok'}, 'examples': {'application/json': [{'squads': [{'id': 3129411261968, 'name': 'Squad 1'}], 'id': 2073711261968, 'name': 'Wing 1'}]}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Content-Language': {'enum': ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'], 'type': 'string', 'description': 'The language used in the response'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of fleet wings'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'get_fleets_fleet_id_wings_404_not_found'}}, 'description': 'Not found', 'title': 'get_fleets_fleet_id_wings_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}}

    def get(self, fleet_id, datasource="tranquility",language="en-us",**kwargs):
        """
                Return information about wings in a fleet
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/wings/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/wings/`
        
        Alternate route: `/dev/fleets/{fleet_id}/wings/`
        
        
        ---
        
        This route is cached for up to 5 seconds

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type datasource: str
        :param datasource: The server name you would like data from
:type language: str
        :param language: Language to use in the response
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "datasource" : datasource, "language" : language, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)

    post_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'post_fleets_fleet_id_wings_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'post_fleets_fleet_id_wings_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'post_fleets_fleet_id_wings_403_forbidden'}}, 'description': 'Forbidden', 'title': 'post_fleets_fleet_id_wings_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.write_fleet.v1'}}, 'description': 'Forbidden'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'post_fleets_fleet_id_wings_404_not_found'}}, 'description': 'Not found', 'title': 'post_fleets_fleet_id_wings_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}, '201': {'schema': {'title': 'post_fleets_fleet_id_wings_created', 'type': 'object', 'properties': {'wing_id': {'format': 'int64', 'type': 'integer', 'description': 'The wing_id of the newly created wing', 'title': 'post_fleets_fleet_id_wings_wing_id'}}, 'description': '201 created object', 'required': ['wing_id']}, 'examples': {'application/json': {'wing_id': 123}}, 'description': 'Wing created'}}

    def post(self, fleet_id, datasource="tranquility",**kwargs):
        """
                Create a new wing in a fleet
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/wings/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/wings/`
        
        Alternate route: `/dev/fleets/{fleet_id}/wings/`

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.post_responses) \
            .post(**kwargs_dict)


class FleetsDetail(object):
    base_url = "https://esi.tech.ccp.is/latest/fleets/{fleet_id}/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_fleets_fleet_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_fleets_fleet_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'get_fleets_fleet_id_403_forbidden'}}, 'description': 'Forbidden', 'title': 'get_fleets_fleet_id_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.read_fleet.v1'}}, 'description': 'Forbidden'}, '200': {'schema': {'title': 'get_fleets_fleet_id_ok', 'type': 'object', 'properties': {'motd': {'type': 'string', 'description': 'Fleet MOTD in CCP flavoured HTML', 'title': 'get_fleets_fleet_id_motd'}, 'is_voice_enabled': {'type': 'boolean', 'description': 'Is EVE Voice enabled', 'title': 'get_fleets_fleet_id_is_voice_enabled'}, 'is_registered': {'type': 'boolean', 'description': 'Does the fleet have an active fleet advertisement', 'title': 'get_fleets_fleet_id_is_registered'}, 'is_free_move': {'type': 'boolean', 'description': 'Is free-move enabled', 'title': 'get_fleets_fleet_id_is_free_move'}}, 'description': '200 ok object', 'required': ['motd', 'is_free_move', 'is_registered', 'is_voice_enabled']}, 'examples': {'application/json': {'motd': 'This is an <b>awesome</b> fleet!', 'is_voice_enabled': False, 'is_registered': False, 'is_free_move': False}}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'Details about a fleet'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'get_fleets_fleet_id_404_not_found'}}, 'description': 'Not found', 'title': 'get_fleets_fleet_id_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}}

    def get(self, fleet_id, datasource="tranquility",**kwargs):
        """
                Return details about a fleet
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/`
        
        Alternate route: `/dev/fleets/{fleet_id}/`
        
        
        ---
        
        This route is cached for up to 5 seconds

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)

    put_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'put_fleets_fleet_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'put_fleets_fleet_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '400': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Bad request message', 'title': 'put_fleets_fleet_id_400_bad_request'}}, 'description': 'Bad request', 'title': 'put_fleets_fleet_id_bad_request'}, 'examples': {'application/json': {'error': 'Bad request message'}}, 'description': 'Invalid request body'}, '204': {'description': 'Fleet updated'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'put_fleets_fleet_id_404_not_found'}}, 'description': 'Not found', 'title': 'put_fleets_fleet_id_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'put_fleets_fleet_id_403_forbidden'}}, 'description': 'Forbidden', 'title': 'put_fleets_fleet_id_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.write_fleet.v1'}}, 'description': 'Forbidden'}}

    def put(self, fleet_id, new_settings, datasource="tranquility",**kwargs):
        """
                Update settings about a fleet
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/`
        
        Alternate route: `/dev/fleets/{fleet_id}/`

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type new_settings: None
        :param new_settings: What to update for this fleet
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "new_settings" : new_settings, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.put_responses) \
            .put(**kwargs_dict)


class FleetsDetailMembersDetail(object):
    base_url = "https://esi.tech.ccp.is/latest/fleets/{fleet_id}/members/{member_id}/"

    delete_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'delete_fleets_fleet_id_members_member_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'delete_fleets_fleet_id_members_member_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'delete_fleets_fleet_id_members_member_id_403_forbidden'}}, 'description': 'Forbidden', 'title': 'delete_fleets_fleet_id_members_member_id_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.write_fleet.v1'}}, 'description': 'Forbidden'}, '204': {'description': 'Fleet member kicked'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'delete_fleets_fleet_id_members_member_id_404_not_found'}}, 'description': 'Not found', 'title': 'delete_fleets_fleet_id_members_member_id_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}}

    def delete(self, fleet_id, member_id, datasource="tranquility",**kwargs):
        """
                Kick a fleet member
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/members/{member_id}/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/members/{member_id}/`
        
        Alternate route: `/dev/fleets/{fleet_id}/members/{member_id}/`

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type member_id: int
        :param member_id: The character ID of a member in this fleet
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "member_id" : member_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.delete_responses) \
            .delete(**kwargs_dict)

    put_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'put_fleets_fleet_id_members_member_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'put_fleets_fleet_id_members_member_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'put_fleets_fleet_id_members_member_id_403_forbidden'}}, 'description': 'Forbidden', 'title': 'put_fleets_fleet_id_members_member_id_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.write_fleet.v1'}}, 'description': 'Forbidden'}, '204': {'description': 'Fleet invitation sent'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'put_fleets_fleet_id_members_member_id_404_not_found'}}, 'description': 'Not found', 'title': 'put_fleets_fleet_id_members_member_id_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}, '422': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'error message', 'title': 'put_fleets_fleet_id_members_member_id_error'}}, 'description': '422 unprocessable entity object', 'title': 'put_fleets_fleet_id_members_member_id_unprocessable_entity'}, 'examples': {'application/json': {'error': 'missing wing_id'}}, 'description': 'Errors in invitation'}}

    def put(self, fleet_id, member_id, movement, datasource="tranquility",**kwargs):
        """
                Move a fleet member around
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/members/{member_id}/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/members/{member_id}/`
        
        Alternate route: `/dev/fleets/{fleet_id}/members/{member_id}/`

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type member_id: int
        :param member_id: The character ID of a member in this fleet
:type movement: None
        :param movement: Details of the invitation
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "member_id" : member_id, "movement" : movement, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.put_responses) \
            .put(**kwargs_dict)


class FleetsDetailSquadsDetail(object):
    base_url = "https://esi.tech.ccp.is/latest/fleets/{fleet_id}/squads/{squad_id}/"

    delete_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'delete_fleets_fleet_id_squads_squad_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'delete_fleets_fleet_id_squads_squad_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'delete_fleets_fleet_id_squads_squad_id_403_forbidden'}}, 'description': 'Forbidden', 'title': 'delete_fleets_fleet_id_squads_squad_id_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.write_fleet.v1'}}, 'description': 'Forbidden'}, '204': {'description': 'Squad deleted'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'delete_fleets_fleet_id_squads_squad_id_404_not_found'}}, 'description': 'Not found', 'title': 'delete_fleets_fleet_id_squads_squad_id_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}}

    def delete(self, fleet_id, squad_id, datasource="tranquility",**kwargs):
        """
                Delete a fleet squad, only empty squads can be deleted
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/squads/{squad_id}/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/squads/{squad_id}/`
        
        Alternate route: `/dev/fleets/{fleet_id}/squads/{squad_id}/`

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type squad_id: int
        :param squad_id: The squad to delete
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "squad_id" : squad_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.delete_responses) \
            .delete(**kwargs_dict)

    put_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'put_fleets_fleet_id_squads_squad_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'put_fleets_fleet_id_squads_squad_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'put_fleets_fleet_id_squads_squad_id_403_forbidden'}}, 'description': 'Forbidden', 'title': 'put_fleets_fleet_id_squads_squad_id_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.write_fleet.v1'}}, 'description': 'Forbidden'}, '204': {'description': 'Squad renamed'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'put_fleets_fleet_id_squads_squad_id_404_not_found'}}, 'description': 'Not found', 'title': 'put_fleets_fleet_id_squads_squad_id_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}}

    def put(self, fleet_id, naming, squad_id, datasource="tranquility",**kwargs):
        """
                Rename a fleet squad
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/squads/{squad_id}/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/squads/{squad_id}/`
        
        Alternate route: `/dev/fleets/{fleet_id}/squads/{squad_id}/`

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type naming: None
        :param naming: New name of the squad
:type squad_id: int
        :param squad_id: The squad to rename
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "naming" : naming, "squad_id" : squad_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.put_responses) \
            .put(**kwargs_dict)


class FleetsDetailWingsDetailSquads(object):
    base_url = "https://esi.tech.ccp.is/latest/fleets/{fleet_id}/wings/{wing_id}/squads/"

    post_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'post_fleets_fleet_id_wings_wing_id_squads_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'post_fleets_fleet_id_wings_wing_id_squads_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'post_fleets_fleet_id_wings_wing_id_squads_403_forbidden'}}, 'description': 'Forbidden', 'title': 'post_fleets_fleet_id_wings_wing_id_squads_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.write_fleet.v1'}}, 'description': 'Forbidden'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'post_fleets_fleet_id_wings_wing_id_squads_404_not_found'}}, 'description': 'Not found', 'title': 'post_fleets_fleet_id_wings_wing_id_squads_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}, '201': {'schema': {'title': 'post_fleets_fleet_id_wings_wing_id_squads_created', 'type': 'object', 'properties': {'squad_id': {'format': 'int64', 'type': 'integer', 'description': 'The squad_id of the newly created squad', 'title': 'post_fleets_fleet_id_wings_wing_id_squads_squad_id'}}, 'description': '201 created object', 'required': ['squad_id']}, 'examples': {'application/json': {'squad_id': 123}}, 'description': 'Squad created'}}

    def post(self, fleet_id, wing_id, datasource="tranquility",**kwargs):
        """
                Create a new squad in a fleet
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/wings/{wing_id}/squads/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/squads/`
        
        Alternate route: `/dev/fleets/{fleet_id}/wings/{wing_id}/squads/`

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type wing_id: int
        :param wing_id: The wing_id to create squad in
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "wing_id" : wing_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.post_responses) \
            .post(**kwargs_dict)


class FleetsDetailWingsDetail(object):
    base_url = "https://esi.tech.ccp.is/latest/fleets/{fleet_id}/wings/{wing_id}/"

    delete_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'delete_fleets_fleet_id_wings_wing_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'delete_fleets_fleet_id_wings_wing_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'delete_fleets_fleet_id_wings_wing_id_403_forbidden'}}, 'description': 'Forbidden', 'title': 'delete_fleets_fleet_id_wings_wing_id_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.write_fleet.v1'}}, 'description': 'Forbidden'}, '204': {'description': 'Wing deleted'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'delete_fleets_fleet_id_wings_wing_id_404_not_found'}}, 'description': 'Not found', 'title': 'delete_fleets_fleet_id_wings_wing_id_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}}

    def delete(self, fleet_id, wing_id, datasource="tranquility",**kwargs):
        """
                Delete a fleet wing, only empty wings can be deleted. The wing may contain squads, but the squads must be empty
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/wings/{wing_id}/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/`
        
        Alternate route: `/dev/fleets/{fleet_id}/wings/{wing_id}/`

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type wing_id: int
        :param wing_id: The wing to delete
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "wing_id" : wing_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.delete_responses) \
            .delete(**kwargs_dict)

    put_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'put_fleets_fleet_id_wings_wing_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'put_fleets_fleet_id_wings_wing_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'put_fleets_fleet_id_wings_wing_id_403_forbidden'}}, 'description': 'Forbidden', 'title': 'put_fleets_fleet_id_wings_wing_id_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.write_fleet.v1'}}, 'description': 'Forbidden'}, '204': {'description': 'Wing renamed'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'put_fleets_fleet_id_wings_wing_id_404_not_found'}}, 'description': 'Not found', 'title': 'put_fleets_fleet_id_wings_wing_id_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}}

    def put(self, fleet_id, naming, wing_id, datasource="tranquility",**kwargs):
        """
                Rename a fleet wing
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/wings/{wing_id}/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/wings/{wing_id}/`
        
        Alternate route: `/dev/fleets/{fleet_id}/wings/{wing_id}/`

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type naming: None
        :param naming: New name of the wing
:type wing_id: int
        :param wing_id: The wing to rename
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "naming" : naming, "wing_id" : wing_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.put_responses) \
            .put(**kwargs_dict)


class FleetsDetailMembers(object):
    base_url = "https://esi.tech.ccp.is/latest/fleets/{fleet_id}/members/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_fleets_fleet_id_members_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_fleets_fleet_id_members_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'get_fleets_fleet_id_members_403_forbidden'}}, 'description': 'Forbidden', 'title': 'get_fleets_fleet_id_members_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.read_fleet.v1'}}, 'description': 'Forbidden'}, '200': {'schema': {'items': {'title': 'get_fleets_fleet_id_members_200_ok', 'type': 'object', 'properties': {'character_id': {'format': 'int32', 'type': 'integer', 'description': 'character_id integer', 'title': 'get_fleets_fleet_id_members_character_id'}, 'role_name': {'type': 'string', 'description': 'Localized role names', 'title': 'get_fleets_fleet_id_members_role_name'}, 'role': {'enum': ['fleet_commander', 'wing_commander', 'squad_commander', 'squad_member'], 'type': 'string', 'description': 'Member�s role in fleet', 'title': 'get_fleets_fleet_id_members_role'}, 'solar_system_id': {'format': 'int32', 'type': 'integer', 'description': 'Solar system the member is located in', 'title': 'get_fleets_fleet_id_members_solar_system_id'}, 'join_time': {'format': 'date-time', 'type': 'string', 'description': 'join_time string', 'title': 'get_fleets_fleet_id_members_join_time'}, 'station_id': {'format': 'int64', 'type': 'integer', 'description': 'Station in which the member is docked in, if applicable', 'title': 'get_fleets_fleet_id_members_station_id'}, 'ship_type_id': {'format': 'int32', 'type': 'integer', 'description': 'ship_type_id integer', 'title': 'get_fleets_fleet_id_members_ship_type_id'}, 'takes_fleet_warp': {'type': 'boolean', 'description': 'Whether the member take fleet warps', 'title': 'get_fleets_fleet_id_members_takes_fleet_warp'}, 'squad_id': {'format': 'int64', 'type': 'integer', 'description': 'ID of the squad the member is in. If not applicable, will be set to -1', 'title': 'get_fleets_fleet_id_members_squad_id'}, 'wing_id': {'format': 'int64', 'type': 'integer', 'description': 'ID of the wing the member is in. If not applicable, will be set to -1', 'title': 'get_fleets_fleet_id_members_wing_id'}}, 'description': '200 ok object', 'required': ['character_id', 'ship_type_id', 'wing_id', 'squad_id', 'role', 'role_name', 'join_time', 'takes_fleet_warp', 'solar_system_id']}, 'type': 'array', 'description': '200 ok array', 'title': 'get_fleets_fleet_id_members_ok'}, 'examples': {'application/json': [{'character_id': 93265215, 'role_name': 'Squad Commander (Boss)', 'role': 'squad_commander', 'solar_system_id': 30003729, 'join_time': '2016-04-29T12:34:56Z', 'station_id': 61000180, 'ship_type_id': 33328, 'takes_fleet_warp': True, 'squad_id': 3129411261968, 'wing_id': 2073711261968}]}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Content-Language': {'enum': ['de', 'en-us', 'fr', 'ja', 'ru', 'zh'], 'type': 'string', 'description': 'The language used in the response'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of fleet members'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'get_fleets_fleet_id_members_404_not_found'}}, 'description': 'Not found', 'title': 'get_fleets_fleet_id_members_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}}

    def get(self, fleet_id, datasource="tranquility",language="en-us",**kwargs):
        """
                Return information about fleet members
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/members/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/members/`
        
        Alternate route: `/dev/fleets/{fleet_id}/members/`
        
        
        ---
        
        This route is cached for up to 5 seconds

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type datasource: str
        :param datasource: The server name you would like data from
:type language: str
        :param language: Language to use in the response
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "datasource" : datasource, "language" : language, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)

    post_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'post_fleets_fleet_id_members_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'post_fleets_fleet_id_members_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '403': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Forbidden message', 'title': 'post_fleets_fleet_id_members_403_forbidden'}}, 'description': 'Forbidden', 'title': 'post_fleets_fleet_id_members_forbidden'}, 'examples': {'application/json': {'error': 'Token is not valid for scope(s): esi-fleets.write_fleet.v1'}}, 'description': 'Forbidden'}, '204': {'description': 'Fleet invitation sent'}, '404': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Not found message', 'title': 'post_fleets_fleet_id_members_404_not_found'}}, 'description': 'Not found', 'title': 'post_fleets_fleet_id_members_not_found'}, 'examples': {'application/json': {'error': 'Not found message'}}, 'description': "The fleet does not exist or you don't have access to it"}, '422': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'error message', 'title': 'post_fleets_fleet_id_members_error'}}, 'description': '422 unprocessable entity object', 'title': 'post_fleets_fleet_id_members_unprocessable_entity'}, 'examples': {'application/json': {'error': 'missing wing_id'}}, 'description': 'Errors in invitation'}}

    def post(self, fleet_id, invitation, datasource="tranquility",**kwargs):
        """
                Invite a character into the fleet, if a character has a CSPA charge set, it is not possible to invite them to the fleet using ESI
        
        ---
        
        Alternate route: `/v1/fleets/{fleet_id}/members/`
        
        Alternate route: `/legacy/fleets/{fleet_id}/members/`
        
        Alternate route: `/dev/fleets/{fleet_id}/members/`

:type fleet_id: int
        :param fleet_id: ID for a fleet
:type invitation: None
        :param invitation: Details of the invitation
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: token, user_agent, X-User-Agent
    """
        kwargs_dict ={
"fleet_id" : fleet_id, "invitation" : invitation, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.post_responses) \
            .post(**kwargs_dict)