from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
import json

app = Flask(__name__)

# API route
@app.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, World!"})

# Route for serving OpenAPI spec
@app.route('/swagger.json')
def swagger_spec():
    with open('swagger.json', 'r') as f:
        return jsonify(json.load(f))

# Configure Swagger UI
SWAGGER_URL = '/docs'
API_URL = '/swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Hello World API"
    }
)

app.register_blueprint(swaggerui_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=8000)