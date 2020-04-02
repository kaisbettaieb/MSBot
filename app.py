from flask import Flask
from config import DevelopmentConfig
from extensions import *
import connexion

def create_app(config):
    """
    creating app
    """
    # Make the WSGI interface available at the top level so wfastcgi can get it.
    connexionApp = connexion.App(__name__, specification_dir='./')
    connexionApp.add_api('swagger.yml')
    connexionApp.app.config.from_object(config)
    connexionApp.app.register_error_handler(500, internal_exception)
    connexionApp.app.register_error_handler(404, page_not_found)
    return connexionApp

def internal_exception(e):
    data = {'Error' : '500, try again later'}
    return data, 500


def page_not_found(e):
    data = {'Error' : '404, page not found, try another page'}
    return data, 404

app = create_app(config=DevelopmentConfig)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3978)
