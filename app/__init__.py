from flask import Flask
from app.models import db
from app.views.user_view import user_bp
from app.views.product_view import product_bp
from app.views.sale_view import sale_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Registrando as rotas
    app.register_blueprint(user_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(sale_bp)

    return app
