from bottle import run
from challenge.app import app

import config

if __name__ == '__main__':
    run(app=app,
        host=config.HOST,
        port=config.PORT,
        reloader=True)
