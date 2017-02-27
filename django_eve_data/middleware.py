"""
Middleware every EveData request Base will be initaliesed by a singleton so you can use the EveData classes on its own
Further it makes it good testable
"""
from .esi_api.base import EsiRequestObject
import inspect


class EveDataMiddleware(object):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if inspect.getattr_static(request.user, 'eve_request_header', None) is not None:
            EsiRequestObject.set_custom_header(getattr(request.user, 'eve_request_header', {}))
