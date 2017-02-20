"""
Middleware every EveData request Base will be initaliesed by a singleton so you can use the EveData classes on its own
Further it makes it good testable
"""
from EveData.esi_api.base import EsiRequestObject


class EveDataMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        EsiRequestObject.set_custom_header(request.user.eve_request_header)
