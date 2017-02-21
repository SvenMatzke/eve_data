import requests
import re
from threading import local


class EsiError(Exception):
    pass


class EsiRequestObject(object):
    _thread_infos = local()

    @classmethod
    def set_custom_header(cls, header):
        """
        :type header:
        """
        old_header = getattr(cls._thread_infos, 'headers', {})
        old_header.update(header)
        setattr(cls._thread_infos, 'headers', old_header)

    def _get_error_message(self, status_code):
        """
        :type status_code: int
        :return: str
        """
        status_response_dict = self._response_dict.get(str(status_code), {})
        return status_response_dict.get('description', "No message defined.")

    def __init__(self, request_url, response_dict, custom_header=None):
        """
        :type request_url: str
        :type response_dict: dict
        """
        if custom_header is not None:
            self.set_custom_header(custom_header)
        self._request_url = request_url
        self._response_dict = response_dict
    
    @staticmethod
    def _get_replaced_url_with_ident(url, **kwargs):
        for name, value in kwargs.items():
            url = re.sub("{%s}" % name, str(value), url)
        return url

    def get(self, **kwargs):
        response = requests.get(
            self._get_replaced_url_with_ident(self._request_url, **kwargs),
            params=kwargs,
            headers=getattr(self._thread_infos, 'headers', {})
        )
        if response.ok:
            return response.json()
        else:
            raise EsiError(self._get_error_message(response.status_code))

    def post(self, **kwargs):
        response = requests.post(
            self._get_replaced_url_with_ident(self._request_url, **kwargs),
            data=kwargs,
            headers=getattr(self._thread_infos, 'headers', {})
        )
        if not response.ok:
            raise EsiError(self._get_error_message(response.status_code))
        return response.json()

    def put(self, **kwargs):
        response = requests.put(
            self._get_replaced_url_with_ident(self._request_url, **kwargs),
            data=kwargs,
            headers=getattr(self._thread_infos, 'headers', {})
        )
        if not response.ok:
            raise EsiError(self._get_error_message(response.status_code))
        return response.json()

    def delete(self, **kwargs):
        response = requests.put(
            self._get_replaced_url_with_ident(self._request_url, **kwargs),
            headers=getattr(self._thread_infos, 'headers', {})
        )
        if not response.ok:
            raise EsiError(self._get_error_message(response.status_code))
        return response.json()
