import json

from demo_sevice import app
from request_handler import RequestHandler
from flask import request, Response


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def api(path):
    """
    :test: requests.get('http://127.0.0.1:5000/',data=json.dumps({'return_value':'great success', 'route':[]}))
    :return:
    """
    # print('args: ', request.args)
    # print('data:', request.data)
    data = json.loads(request.data.decode("utf-8"))
    handler = RequestHandler(data=data)
    return_value = handler.send_request_to_next_service()
    # print('return-value={}'.format(return_value))
    return Response(response=return_value, status=200, mimetype="application/json")