import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configurações básicas do Flask carregadas do ambiente."""
    
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-key-default")
    
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False