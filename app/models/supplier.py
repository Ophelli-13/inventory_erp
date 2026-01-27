import uuid
from app.database.connection import db

class Supplier(db.Model):
    __tablename__ = 'suppliers'
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = db.Column(db.String(150), nullable=False)
    contact_email = db.Column(db.String(120), unique=True)
    phone = db.Column(db.String(20))
    products = db.relationship('Product', backref='supplier', lazy=True)