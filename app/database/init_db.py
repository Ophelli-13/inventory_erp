from app.database.connection import db, migrate
from app.models.category import Category
from app.models.supplier import Supplier
from app.models.product import Product
from app.models.stock_movement import StockMovement


def init_db(app):
    """Inicia o banco de dados"""
    db.init_app(app)
    migrate.init_app(app, db)