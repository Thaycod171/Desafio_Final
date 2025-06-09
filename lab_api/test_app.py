from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import os

app = Flask(__name__)

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'your_secret_key')
jwt = JWTManager(app)

### Swagger UI ###
SWAGGER_URL = '/swagger'
API_DOC_URL = '/static/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_DOC_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/')
def home():
    return jsonify(message="API is running")

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items=["item1", "item2", "item3"])

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify(message="Username e password são obrigatórios"), 400

    # Simula um usuário existente
    if username == 'admin':
        return jsonify(message="Usuário já registrado"), 409

    # Simula um cadastro com sucesso
    return jsonify(message="Usuário registrado com sucesso"), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username', None)
    password = data.get('password', None)

    # Autenticação simulada
    if username == 'admin' and password == '1234':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify(msg="Usuário ou senha incorretos"), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="Protected route")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 1313))
    app.run(host='0.0.0.0', port=port)
