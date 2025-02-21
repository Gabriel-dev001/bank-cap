from flask import Blueprint, request, jsonify
from app import db  # Importando a conexão com o banco
from app.models.test import Test  # Importando o modelo Test

# Criando um Blueprint para o Controller
api_controller = Blueprint("test_controller", __name__)

# Rota para verificar se a API está rodando
@api_controller.route('/', methods=['GET'])
def home():
    return jsonify({"teste1": "teste",
                   "teste2": "teste2"}), 200

# Rota para buscar todos os registros da tabela "test"
@api_controller.route("/tests", methods=["GET"])
def get_tests():
    try:
        tests = Test.query.all()  # Busca todos os registros da tabela
        return jsonify([{"id": t.id, "name": t.name} for t in tests]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
