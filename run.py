#!python
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from demo_sevice import app


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) > 1:
        print('error number of params: {}'.format(args))
        sys.exit(-1)

    port = 5000
    if args:
        port = args[0]

    app.run(host='0.0.0.0', port=port)
