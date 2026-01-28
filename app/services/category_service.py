from app.database.connection import db
from app.models.category import Category

class CategoryService:
    @staticmethod
    def create_category(name, description=None):
        
        category = Category(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def get_all():
        return Category.query.all()