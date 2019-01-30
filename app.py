from flask import Flask
import utils

server = Flask(__name__)
apps = ['dataview', 'graphview']
apps_dict = {x: utils.create_dash_app(server, x) for x in apps}


@server.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    server.run()
