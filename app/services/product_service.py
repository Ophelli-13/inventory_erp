from app.database.connection import db
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
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update_stock(product_id, quantity, movement_type, reason):
       
        product = Product.query.get(product_id)
        if not product:
            raise Exception("Produto não encontrado")

        if movement_type == 'OUT' and product.stock_quantity < quantity:
            raise Exception("Estoque insuficiente para esta saída")

        
        if movement_type == 'IN':
            product.stock_quantity += quantity
        else:
            product.stock_quantity -= quantity

        
        movement = StockMovement(
            product_id=product_id,
            type=movement_type,
            quantity=quantity,
            reason=reason
        )

        db.session.add(movement)
        db.session.commit()
        return product