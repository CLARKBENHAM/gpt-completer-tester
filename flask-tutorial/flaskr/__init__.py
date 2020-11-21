# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 23:10:32 2020

@author: student
"""

import os

from flask import Flask

#why do use an application factory?
#so can have multple instances?
#why get_db() rigamarole?
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # register the database commands
    from flaskr import db
    db.init_app(app)
    
    from . import auth
    app.register_blueprint(auth.bp)
    
    return app


