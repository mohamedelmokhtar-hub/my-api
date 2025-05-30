from flask import Flask  # type: ignore
from flask_sqlalchemy import SQLAlchemy  # type: ignore

db = SQLAlchemy()
db_name = 'mokhtar'

def create_app():
    app = Flask(__name__)
    print("Flask app instance created")

    app.config['SECRET_KEY'] = 'Mokhtars_api'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:06082004@localhost/{db_name}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .view import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    from .models import User, Note

    with app.app_context():
        db.create_all()

    return app