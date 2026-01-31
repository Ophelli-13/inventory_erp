from app.repositories.product_repository import ProductRepository

class InventoryService:
    @staticmethod
    def get_low_stock_report(threshold=5):
        """[x] Alerta de estoque mínimo: Lista produtos abaixo do limite."""
        all_products = ProductRepository.get_all()
        return [p for p in all_products if p.stock_quantity < threshold]

    @staticmethod
    def calculate_inventory_value():
        all_products = ProductRepository.get_all()
        return sum(p.price * p.stock_quantity for p in all_products)