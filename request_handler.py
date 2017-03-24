import json
import requests


class RequestHandler:
    def __init__(self, data):
        self._data = data
        self._route = self._data.get('route', None)

    def send_request_to_next_service(self):
        if len(self._route):
            next_hop_params = self._route.pop(0)
            print('next-hop: ', next_hop_params)
            return self._build_url_and_send_request(next_hop_params)
        else:
            return json.dumps(self._data.get('return_value', {'value':'success'}))

    def _build_url_and_send_request(self, params):
        ip = params.get('ip')
        port = params.get('port')
        http_type = params.get('type')
        path = params.get('path', '')
        url = 'http://' + ip + ':' + port + '/' + path
        print('next-hop url: {} data: {}'.format(url, self._data))
        return self._send_request(http_type, url, self._data)

    def _send_request(self, http_type, url, request_data):
        request = None
        data = json.dumps(request_data)
        if http_type == 'get':
            request = requests.get(url, data=data)
        elif http_type == 'post':
            request = requests.post(url, data=data)
        else:
            raise Exception

        if request:
            return request.text