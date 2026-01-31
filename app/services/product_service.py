from app.repositories.product_repository import ProductRepository
from app.repositories.stock_movement_repository import StockMovementRepository
from app.exceptions.stock_exception import InsufficientStockError
from app.models.product import Product
from app.models.stock_movement import StockMovement

class ProductService:
    
    @staticmethod
    def create_product(data):
       
        product = Product(
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            stock_quantity=data.get('stock_quantity', 0),
            category_id=data.get('category_id'),
            supplier_id=data.get('supplier_id')
        )
        return ProductRepository.save(product)

    @staticmethod
    def update_stock(product_id, quantity, movement_type, reason):

        product = ProductRepository.get_by_id(product_id)
        if not product:
            raise Exception("Produto não encontrado.")

        # [x] Validação de estoque negativo
        if movement_type == 'OUT' and product.stock_quantity < quantity:
 
            raise InsufficientStockError(
                f"Saldo insuficiente! {product.name} possui apenas {product.stock_quantity} unidades."
            )

        
        if movement_type == 'IN':
            product.stock_quantity += quantity
        else:
            product.stock_quantity -= quantity

        # [x] Alerta de estoque mínimo
        if product.stock_quantity < 5:
            # No futuro, aqui poderíamos disparar um e-mail ou log de sistema
            print(f"⚠️ SISTEMA: Estoque crítico para {product.name} ({product.stock_quantity} un).")

        # [x] Registro de movimentação (StockMovementService/Repository)
        movement = StockMovement(
            product_id=product_id,
            type=movement_type,
            quantity=quantity,
            reason=reason
        )
        
        StockMovementRepository.save(movement)
        return ProductRepository.save(product)

    @staticmethod
    def get_product_details(product_id):
        return ProductRepository.get_by_id(product_id)

    @staticmethod
    def list_all_products():
        return ProductRepository.get_all()