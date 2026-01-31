from app.repositories.stock_movement_repository import StockMovementRepository

class StockMovementService:
    @staticmethod
    def get_history(product_id=None):
        if product_id:
            return StockMovementRepository.get_by_product(product_id)
        return StockMovementRepository.get_all()