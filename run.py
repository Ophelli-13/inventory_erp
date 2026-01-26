from flask import Flask, jsonify
from app.config.settings import Config
from app.database.init_db import init_db
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    init_db(app)


    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({
            "status": "online",
            "database": "connected",
            "message": "Inventory ERP pronto para o próximo passo!"
        }), 200

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)