from app.database.connection import db
from app.models.supplier import Supplier

class SupplierService:
    @staticmethod
    def create_supplier(name, email=None, phone=None):
        supplier = Supplier(name=name, contact_email=email, phone=phone)
        db.session.add(supplier)
        db.session.commit()
        return supplier