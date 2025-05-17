from flask import Flask
from extensions import db
from routes import app as app_routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = 'some_secret_key'
    db.init_app(app)
    app.register_blueprint(app_routes)

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=False)