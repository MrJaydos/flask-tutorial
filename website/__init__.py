from flask import Flask

def create_app():
    app = Flask(__name__)
    # Initialised secret key
    app.config['SECRET_KEY'] = 'SECRETKEY'

    return app
