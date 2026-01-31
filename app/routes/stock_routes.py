from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.schemas.stock_schema import StockMovementSchema
from app.exceptions.stock_exception import InsufficientStockError

stock_bp = Blueprint('stock_bp', __name__)

@stock_bp.route('/stock/move', methods=['POST'])
def move_stock():
    data = request.get_json()
    
    errors = StockMovementSchema.validate_movement(data)
    if errors:
        return jsonify({"errors": errors}), 400
        
    try:
        product = ProductService.update_stock(
            product_id=data.get('product_id'),
            quantity=data.get('quantity'),
            movement_type=data.get('type'),
            reason=data.get('reason')
        )
        return jsonify({
            "message": "Movimentação realizada",
            "new_stock": product.stock_quantity
        }), 200
    except InsufficientStockError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Erro interno no servidor"}), 500