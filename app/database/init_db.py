from app.database.connection import db, migrate


def init_db(app):
    """Inicia o banco de dados"""
    db.init_app(app)
    migrate.init_app(app, db)