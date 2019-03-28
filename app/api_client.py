import requests
import logging
from typing import Dict
from utils.utils import delay as make_delay


def http_response(decorated):
    def decorator(instance, *args, **kwargs):
        return HttpResponse(decorated(instance, *args, **kwargs))
    return decorator


class HttpResponse:

    def __init__(self, response: requests.Response):
        self._response = response

    @property
    def code(self) -> int:
        return self._response.status_code

    @property
    def body(self) -> str:
        return self._response.text

    @property
    def json(self) -> Dict:
        return self._response.json()


class HttpClient:

    def __init__(self, config, method_chain=None):
        """
        API client with fluent interface

        Example::
            ``HttpClient(config).api.tasks.param(123).get()``
            GET <api_url>/api/tasks/123

        :param config: :class:`config.TodoistApi.Settings`
        """
        self._method_chain = method_chain or ['']
        self._config = config

    def param(self, param):
        return self._get_client(str(param))

    @http_response  # wrap :class:`requests.Response` object to :class:`app.api_client.HttpResponse`
    def get(self):
        return self._request('get')

    @make_delay  # delay for avoiding 500 error (maybe DDOS protection)
    @http_response
    def post(self, payload):
        return self._request('post', json=payload)

    @make_delay  # delay for avoiding 500 error (maybe DDOS protection)
    @http_response
    def delete(self):
        return self._request('delete')

    def __getattr__(self, item):
        return self._get_client(item)

    def _get_client(self, method):
        return HttpClient(self._config, method_chain=self._method_chain + [method])

    def _get_method(self):
        return '/'.join(self._method_chain)

    def _get_header(self, **kwargs):
        header = {
            'Authorization': self._config.auth,
            'Accept': self._config.content
        }
        if kwargs.get('json'):
            header['Content-Type'] = self._config.content
        return header

    def _request(self, method, **kwargs):
        self._logger.info('request: {} {} kwargs: {}'.format(method, self._config.base_url + self._get_method(), kwargs))
        response = requests.request(
            method,
            self._config.base_url + self._get_method(),
            headers=self._get_header(),
            **kwargs
        )
        self._logger.info('response {}, {}'.format(response.status_code, response.text))
        return response

    @property
    def _logger(self):
        return logging.getLogger('app.api_client.HttpClient')

    @property
    def delay(self):
        return self._config.delay
