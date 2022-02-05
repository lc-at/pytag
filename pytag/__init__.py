from flask import Flask


def create_app():
    app = Flask(__name__)

    from .models import db

    db.init_app(app)

    from .views import bp as views_bp  # noqa

    app.register_blueprint(views_bp)

    return app

