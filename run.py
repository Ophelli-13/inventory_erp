from flask import Flask, jsonify
from app.config.settings import Config
from app.database.init_db import init_db
from app.routes.product_routes import product_bp
from app.routes.stock_routes import stock_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    app.register_blueprint(product_bp, url_prefix='/api')
    app.register_blueprint(stock_bp, url_prefix='/api')
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"error": "Recurso não encontrado"}), 404

    @app.errorhandler(500)
    def internal_server(error):
        return jsonify({"error": "Erro interno no servidor"}), 500

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)