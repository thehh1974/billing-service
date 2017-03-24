import json
import sys

from request_handler import RequestHandler


def read_json_file(file_name):
    with open(file_name) as data_file:
        # a = data_file.read()
        # print(a)
        data = json.load(data_file)
        print(data)
        return data


if __name__ == '__main__':
    file_name = './data/request_info.json'
    args = sys.argv[1:]
    if len(args) > 1:
        print('error number of params: {}'.format(args))
        sys.exit(-1)

    if args:
        file_name = args[0]

    data = read_json_file(file_name)
    handler = RequestHandler(data=data)
    return_value = handler.send_request_to_next_service()
    print('return-value: {}'.format(return_value))
