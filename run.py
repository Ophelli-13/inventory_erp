from flask import Flask, jsonify
from app.config.settings import Config

def create_app():
    app= Flask(__name__)

    app.config.from_object(Config)

    @app.route('/health', methods=["GET"])
    def health():
        return jsonify({
            "status": "online",
            "message": "Iventory ERP API está rodando",
            "version": "1.0.0"
        }), 200
    return app


app= create_app()

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)