from app.models.stock_movement import StockMovement
from app.database.connection import db

class StockMovementRepository:
    @staticmethod
    def save(movement):
        db.session.add(movement)
        db.session.commit()
        return movement

    @staticmethod
    def get_by_product(product_id):
        return StockMovement.query.filter_by(product_id=product_id).order_by(StockMovement.created_at.desc()).all()

    @staticmethod
    def get_all():
        return StockMovement.query.order_by(StockMovement.created_at.desc()).all()