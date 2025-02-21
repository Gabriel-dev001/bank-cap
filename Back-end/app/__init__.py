from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Configuração básica do Flask
    app.config["SECRET_KEY"] = "minha_chave_super_secreta"

    # Registrar o Controller (Blueprint) com o prefixo "/api"
    from app.controllers.test_controller import api_controller
    app.register_blueprint(api_controller, url_prefix='/api')

    # Instaciando Banco
    db.init_app(app)

    return app
