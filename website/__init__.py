from flask import Flask # type: ignore

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='Mokhtars_api'
    from .view import views
    from .auth import auth
    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/auth')

    return app