# coding utf-8
"""
Autogenerated Template File
"""

from .base import EsiRequestObject


class Incursions(object):
    base_url = "https://esi.tech.ccp.is/latest/incursions/"

    get_responses = {'500': {'schema': {'type': 'object', 'properties': {'error': {'type': 'string', 'description': 'Internal server error message', 'title': 'get_incursions_500_internal_server_error'}}, 'description': 'Internal server error', 'title': 'get_incursions_internal_server_error'}, 'examples': {'application/json': {'error': "uncaught exception: IOError('out of memory')"}}, 'description': 'Internal server error'}, '200': {'schema': {'items': {'title': 'get_incursions_200_ok', 'type': 'object', 'properties': {'state': {'enum': ['withdrawing', 'mobilizing', 'established'], 'type': 'string', 'description': 'The state of this incursion', 'title': 'get_incursions_state'}, 'influence': {'format': 'float', 'type': 'number', 'description': 'Influence of this incursion as a float from 0 to 1', 'title': 'get_incursions_influence'}, 'constellation_id': {'format': 'int32', 'type': 'integer', 'description': 'The constellation id in which this incursion takes place', 'title': 'get_incursions_constellation_id'}, 'faction_id': {'format': 'int32', 'type': 'integer', 'description': "The attacking faction's id", 'title': 'get_incursions_faction_id'}, 'has_boss': {'type': 'boolean', 'description': 'Whether the final encounter has boss or not', 'title': 'get_incursions_has_boss'}, 'type': {'type': 'string', 'description': 'The type of this incursion', 'title': 'get_incursions_type'}, 'infested_solar_systems': {'items': {'format': 'int32', 'type': 'integer', 'description': 'infested_solar_system integer', 'title': 'get_incursions_infested_solar_system'}, 'type': 'array', 'description': 'A list of infested solar system ids that are a part of this incursion', 'title': 'get_incursions_infested_solar_systems'}, 'staging_solar_system_id': {'format': 'int32', 'type': 'integer', 'description': 'Staging solar system for this incursion', 'title': 'get_incursions_staging_solar_system_id'}}, 'description': '200 ok object', 'required': ['type', 'state', 'influence', 'has_boss', 'faction_id', 'constellation_id', 'staging_solar_system_id', 'infested_solar_systems']}, 'type': 'array', 'description': '200 ok array', 'title': 'get_incursions_ok'}, 'examples': {'application/json': [{'state': 'mobilizing', 'influence': 1.0, 'constellation_id': 20000607, 'faction_id': 500019, 'has_boss': True, 'type': 'Incursion', 'infested_solar_systems': [30004148, 30004149, 30004150, 30004151, 30004152, 30004153, 30004154], 'staging_solar_system_id': 30004154}]}, 'headers': {'Expires': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}, 'Cache-Control': {'type': 'string', 'description': 'The caching mechanism used'}, 'Last-Modified': {'type': 'string', 'description': 'RFC7231 formatted datetime string'}}, 'description': 'A list of incursions'}}

    def get(self, datasource="tranquility",**kwargs):
        """
                Return a list of current incursions
        
        ---
        
        Alternate route: `/v1/incursions/`
        
        Alternate route: `/legacy/incursions/`
        
        Alternate route: `/dev/incursions/`
        
        
        ---
        
        This route is cached for up to 300 seconds

:type datasource: str
        :param datasource: The server name you would like data from
:param kwargs: user_agent, X-User-Agent
    """
        kwargs_dict ={
"datasource" : datasource, 
        }
        kwargs_dict.update(kwargs)
        return EsiRequestObject(self.base_url, self.get_responses) \
            .get(**kwargs_dict)