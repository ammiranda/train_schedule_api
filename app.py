from flask import Flask, Response, json, jsonify, request
from marshmallow import Schema, fields, ValidationError
from marshmallow.validate import Regexp

from db import Database

app = Flask(__name__)

inner_db = SQLAlchemy(app)
db = Database(inner_db)


class TrainSchema(Schema):
    id = fields.String(required=True, validate=Regexp(r"^[a-zA-Z0-9]{1,4}$"))
    schedules = fields.List(fields.Time(), required=True)


@app.route('/')
def init():
    return "OK"


@app.route('/trains', methods=['POST'])
def add_train():
    request_data = request.json
    schema = TrainSchema()
    try:
        result = schema.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # try:
    #     db.set(result.key, result)
    # except:

    return jsonify(result)


@app.route('/trains/<string:train_id>')
def get_schedule(train_id):
    return
    # try:
    #     train = db.get(train_id)
    # # except


@app.route('/trains/next')
def get_next():
    """ Implement a route that returns the next time multiple trains are in the station """
    raise NotImplementedError


if __name__ == '__main__':
    app.run(host='0.0.0.0')
