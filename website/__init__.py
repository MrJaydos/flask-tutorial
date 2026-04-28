from flask import Flask

def create_app():
    app = Flask(__name__)
    # Initialised secret key
    app.config['SECRET_KEY'] = 'SECRETKEY'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
