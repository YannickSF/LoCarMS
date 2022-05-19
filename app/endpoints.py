
from flask import Flask, request
from flask_cors import CORS
from app.domain import Domain

app = Flask(__name__)
cors = CORS(app)

ctx = Domain()


@app.route("/")
def index():
    # validate origin
    return {'status': 200}


@app.route("/cars", methods=['POST'])
def post_car():
    if request.method == 'POST':
        return {'response': ctx.create_car(**request.get_json())}

    return {'error': 'method not allow.'}


@app.route("/cars", methods=['GET'])
def get_cars():
    if request.method == 'GET':
        return {'response': ctx.read_car()}

    return {'error': 'method not allow.'}


@app.route("/cars/<string:id>", methods=['GET'])
def get_car_by_id(id):
    if request.method == 'GET':
        return {'response': ctx.read_car_by_id(id)}

    return {'error': 'method not allow.'}


@app.route("/cars/<string:id>", methods=['PUT'])
def put_car(id):
    if request.method == 'PUT':
        return {'response': ctx.update_car(id, **request.get_json())}

    return {'error': 'method not allow.'}


@app.route("/cars/<string:id>", methods=['DELETE'])
def delete_car_by_id(id):
    if request.method == 'DELETE':
        return {'response': ctx.delete_(id)}

    return {'error': 'method not allow.'}


@app.route("/announces", methods=['POST'])
def post_announce():
    if request.method == 'POST':
        return {'response': ctx.create_announce(**request.get_json())}

    return {'error': 'method not allow.'}


@app.route("/announces", methods=['GET'])
def get_announces():
    if request.method == 'GET':
        return {'response': ctx.read_announce()}

    return {'error': 'method not allow.'}


@app.route("/announces/<string:id>", methods=['GET'])
def get_announce_by_id(id):
    if request.method == 'GET':
        return {'response': ctx.read_announce_by_id(id)}

    return {'error': 'method not allow.'}


@app.route("/announces/<string:id>", methods=['PUT'])
def put_announce(id):
    if request.method == 'PUT':
        return {'response': ctx.update_announce(id, **request.get_json())}

    return {'error': 'method not allow.'}


@app.route("/announces/<string:id>", methods=['DELETE'])
def delete_announce_by_id(id):
    if request.method == 'DELETE':
        return {'response': ctx.delete_announce(id)}

    return {'error': 'method not allow.'}


@app.route("/locations", methods=['POST'])
def post_location():
    if request.method == 'POST':
        return {'response': ctx.create_location(**request.get_json())}

    return {'error': 'method not allow.'}


@app.route("/locations", methods=['GET'])
def get_locations():
    if request.method == 'GET':
        return {'response': ctx.read_location()}

    return {'error': 'method not allow.'}


@app.route("/locations/<string:id>", methods=['GET'])
def get_location_by_id(id):
    if request.method == 'GET':
        return {'response': ctx.read_location_by_id(id)}

    return {'error': 'method not allow.'}


@app.route("/locations/<string:id>", methods=['PUT'])
def put_location(id):
    if request.method == 'PUT':
        return {'response': ctx.update_location(id, **request.get_json())}

    return {'error': 'method not allow.'}


@app.route("/locations/<string:id>", methods=['DELETE'])
def delete_location_by_id(id):
    if request.method == 'DELETE':
        return {'response': ctx.delete_location(id)}

    return {'error': 'method not allow.'}
