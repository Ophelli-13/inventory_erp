from flask import Blueprint, request, jsonify
from app.services.product_service import ProductService
from app.schemas.product_schema import ProductSchema
from app.exceptions.stock_exception import InsufficientStockError

product_bp = Blueprint('product_bp', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    products = ProductService.list_all_products()
    return jsonify([{
        "id": p.id, 
        "name": p.name, 
        "price": float(p.price), 
        "stock": p.stock_quantity
    } for p in products]), 200

@product_bp.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    
    errors = ProductSchema.validate_create(data)
    if errors:
        return jsonify({"errors": errors}), 400
        
    product = ProductService.create_product(data)
    return jsonify({"id": product.id, "message": "Produto criado com sucesso"}), 201