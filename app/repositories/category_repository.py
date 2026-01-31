from app.models.category import Category
from app.database.connection import db

class CategoryRepository:
    @staticmethod
    def save(category):
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def get_all():
        return Category.query.all()

    @staticmethod
    def get_by_id(id):
        return Category.query.get(id)