from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importando os modelos
from .user import User
from .product import Product
from .sale import Sale
