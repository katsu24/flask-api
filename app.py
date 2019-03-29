from flask import Flask, jsonify, abort, make_response

api = Flask(__name__)


@api.route('/get', methods=['GET'])
def get():
    result = { "greeting": 'hello Flask'}
    return make_response(jsonify(result))


@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3001)