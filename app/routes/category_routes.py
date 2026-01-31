from flask import Blueprint, request, jsonify
from app.services.category_service import CategoryService
from app.schemas.category_schema import CategorySchema

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = CategoryService.get_all()
    return jsonify([{
        "id": c.id,
        "name": c.name,
        "description": c.description
    } for c in categories]), 200

@category_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    errors = CategorySchema.validate_create(data)
    if errors:
        return jsonify({"errors": errors}), 400
    
    category = CategoryService.create_category(
        name=data.get('name'),
        description=data.get('description')
    )
    return jsonify({"id": category.id, "message": "Categoria criada com sucesso"}), 201