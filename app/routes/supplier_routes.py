from flask import Blueprint, request, jsonify
from app.services.supplier_service import SupplierService
from app.schemas.supplier_schema import SupplierSchema

supplier_bp = Blueprint('supplier_bp', __name__)

@supplier_bp.route('/suppliers', methods=['GET'])
def get_suppliers():
    suppliers = SupplierService.get_all()
    return jsonify([{
        "id": s.id,
        "name": s.name,
        "email": s.contact_email,
        "phone": s.phone
    } for s in suppliers]), 200

@supplier_bp.route('/suppliers', methods=['POST'])
def create_supplier():
    data = request.get_json()
    errors = SupplierSchema.validate_create(data)
    if errors:
        return jsonify({"errors": errors}), 400
    
    supplier = SupplierService.create_supplier(
        name=data.get('name'),
        email=data.get('contact_email'),
        phone=data.get('phone')
    )
    return jsonify({"id": supplier.id, "message": "Fornecedor criado com sucesso"}), 201