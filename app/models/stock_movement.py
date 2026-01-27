import uuid
from datetime import datetime
from app.database.connection import db

class StockMovement(db.Model):
    __tablename__ = 'stock_movements'

    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    
    product_id = db.Column(db.String(36), db.ForeignKey('products.id'), nullable=False)
    
    type = db.Column(db.String(10), nullable=False) 
    
    quantity = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(255))
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    
    def __repr__(self):
        return f'<StockMovement {self.type} - {self.quantity} units of Product {self.product_id}>'