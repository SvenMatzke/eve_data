# coding utf-8
"""
Autogenerated Template File
"""

from .base import EsiRequestObject


class WarsDetail(object):
    base_url = "https://esi.tech.ccp.is/latest/wars/{war_id}/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_wars_war_id_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_wars_war_id_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'title': 'get_wars_war_id_ok', 'type': 'object', 'properties': {'declared': {'format': 'date-time', 'type': 'string', 'description': 'Time that the war was declared', 'title': 'get_wars_war_id_declared'}, 'started': {'format': 'date-time', 'type': 'string', 'description': 'Time when the war started and both sides could shoot each other', 'title': 'get_wars_war_id_started'}, 'allies': {'items': {'type': 'object', 'properties': {'corporation_id': {'format': 'int32', 'type': 'integer', 'description': 'Corporation ID if and only if this ally is a corporation', 'title': 'get_wars_war_id_corporation_id'}, 'alliance_id': {'format': 'int32', 'type': 'integer', 'description': 'Alliance ID if and only if this ally is an alliance', 'title': 'get_wars_war_id_alliance_id'}}, 'description': 'ally object', 'title': 'get_wars_war_id_ally'}, 'type': 'array', 'description': 'allied corporations or alliances, each object contains either corporation_id or alliance_id', 'title': 'get_wars_war_id_allies'}, 'aggressor': {'title': 'get_wars_war_id_aggressor', 'type': 'object', 'properties': {'corporation_id': {'format': 'int32', 'type': 'integer', 'description': 'Corporation ID if and only if the aggressor is a corporation', 'title': 'get_wars_war_id_corporation_id'}, 'ships_killed': {'format': 'int32', 'type': 'integer', 'description': 'The number of ships the aggressor has killed', 'title': 'get_wars_war_id_ships_killed'}, 'alliance_id': {'format': 'int32', 'type': 'integer', 'description': 'Alliance ID if and only if the aggressor is an alliance', 'title': 'get_wars_war_id_alliance_id'}, 'isk_destroyed': {'format': 'float', 'type': 'number', 'description': 'ISK value of ships the aggressor has destroyed', 'title': 'get_wars_war_id_isk_destroyed'}}, 'description': 'The aggressor corporation or alliance that declared this war, only contains either corporation_id or alliance_id', 'required': ['ships_killed', 'isk_destroyed']}, 'finished': {'format': 'date-time', 'type': 'string', 'description': 'Time the war ended and shooting was no longer allowed', 'title': 'get_wars_war_id_finished'}, 'id': {'format': 'int32', 'type': 'integer', 'description': 'ID of the specified war', 'title': 'get_wars_war_id_id'}, 'mutual': {'type': 'boolean', 'description': 'Was the war declared mutual by both parties', 'title': 'get_wars_war_id_mutual'}, 'open_for_allies': {'type': 'boolean', 'description': 'Is the war currently open for allies or not', 'title': 'get_wars_war_id_open_for_allies'}, 'defender': {'title': 'get_wars_war_id_defender', 'type': 'object', 'properties': {'corporation_id': {'format': 'int32', 'type': 'integer', 'description': 'Corporation ID if and only if the defender is a corporation', 'title': 'get_wars_war_id_corporation_id'}, 'ships_killed': {'format': 'int32', 'type': 'integer', 'description': 'The number of ships the defender has killed', 'title': 'get_wars_war_id_ships_killed'}, 'alliance_id': {'format': 'int32', 'type': 'integer', 'description': 'Alliance ID if and only if the defender is an alliance', 'title': 'get_wars_war_id_alliance_id'}, 'isk_destroyed': {'format': 'float', 'type': 'number', 'description': 'ISK value of ships the defender has killed', 'title': 'get_wars_war_id_isk_destroyed'}}, 'description': 'The defending corporation or alliance that declared this war, only contains either corporation_id or alliance_id', 'required': ['ships_killed', 'isk_destroyed']}, 'retracted': {'format': 'date-time', 'type': 'string', 'description': 'Time the war was retracted but both sides could still shoot each other', 'title': 'get_wars_war_id_retracted'}}, 'description': '200 ok object', 'required': ['id', 'declared', 'mutual', 'open_for_allies', 'aggressor', 'defender']}, 'examples': {'application/json': {'declared': '2004-05-22T05:20:00Z', 'aggressor': {'corporation_id': 986665792, 'ships_killed': 0, 'isk_destroyed': 0}, 'id': 1941, 'mutual': False, 'open_for_allies': False, 'defender': {'corporation_id': 1001562011, 'ships_killed': 0, 'isk_destroyed': 0}}}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'Details about a war'}, '422': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Unprocessable entity message', 'title': 'get_wars_war_id_422_unprocessable_entity'}}, 'description': 'Unprocessable entity', 'title': 'get_wars_war_id_unprocessable_entity'}, 'examples': {'application/json': {'error': 'Unprocessable entity message'}}, 'description': 'War not found'}}

    def get(self, war_id, datasource="tranquility",**kwargs):
        """
                Return details about a war
        
        ---
        
        Alternate route: `/v1/wars/{war_id}/`
        
        Alternate route: `/legacy/wars/{war_id}/`
        
        Alternate route: `/dev/wars/{war_id}/`
        
        
        ---
        
        This route is cached for up to 3600 seconds

:type war_id: int
        :param war_id: ID for a war
:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: user_agent, X-User-Agent
    """
        kwargs_dict ={
"war_id" : war_id, "datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)


class WarsDetailKillmails(object):
    base_url = "https://esi.tech.ccp.is/latest/wars/{war_id}/killmails/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_wars_war_id_killmails_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_wars_war_id_killmails_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'items': {'title': 'get_wars_war_id_killmails_200_ok', 'type': 'object', 'properties': {'killmail_id': {'format': 'int32', 'type': 'integer', 'description': 'ID of this killmail', 'title': 'get_wars_war_id_killmails_killmail_id'}, 'killmail_hash': {'type': 'string', 'description': 'A hash of this killmail', 'title': 'get_wars_war_id_killmails_killmail_hash'}}, 'description': '200 ok object', 'required': ['killmail_id', 'killmail_hash']}, 'type': 'array', 'description': '200 ok array', 'title': 'get_wars_war_id_killmails_ok'}, 'examples': {'application/json': [{'killmail_id': 2, 'killmail_hash': '8eef5e8fb6b88fe3407c489df33822b2e3b57a5e'}, {'killmail_id': 1, 'killmail_hash': 'b41ccb498ece33d64019f64c0db392aa3aa701fb'}]}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of killmail IDs and hashes'}, '422': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Unprocessable entity message', 'title': 'get_wars_war_id_killmails_422_unprocessable_entity'}}, 'description': 'Unprocessable entity', 'title': 'get_wars_war_id_killmails_unprocessable_entity'}, 'examples': {'application/json': {'error': 'Unprocessable entity message'}}, 'description': 'War not found'}}

    def get(self, war_id, datasource="tranquility",page=1,**kwargs):
        """
                Return a list of kills related to a war
        
        ---
        
        Alternate route: `/v1/wars/{war_id}/killmails/`
        
        Alternate route: `/legacy/wars/{war_id}/killmails/`
        
        Alternate route: `/dev/wars/{war_id}/killmails/`
        
        
        ---
        
        This route is cached for up to 3600 seconds

:type war_id: int
        :param war_id: A valid war ID
:type datasource: str
        :param datasource: The server name you would like data from
:type page: int
        :param page: Which page to query, starting at 1, 2000 killmails per page.
:param kwargs: user_agent, X-User-Agent
    """
        kwargs_dict ={
"war_id" : war_id, "datasource" : datasource, "page" : page, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)


class Wars(object):
    base_url = "https://esi.tech.ccp.is/latest/wars/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_wars_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_wars_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'items': {'format': 'int32', 'type': 'integer', 'description': '200 ok integer', 'title': 'get_wars_200_ok'}, 'type': 'array', 'description': '200 ok array', 'title': 'get_wars_ok'}, 'examples': {'application/json': [3, 2, 1]}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of war IDs, 2000 at most, in decending order by war_id.'}}

    def get(self, datasource="tranquility",**kwargs):
        """
                Return a list of wars
        
        ---
        
        Alternate route: `/v1/wars/`
        
        Alternate route: `/legacy/wars/`
        
        Alternate route: `/dev/wars/`
        
        
        ---
        
        This route is cached for up to 3600 seconds

:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: max_war_id, user_agent, X-User-Agent
    """
        kwargs_dict ={
"datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)