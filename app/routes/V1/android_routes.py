import flask
from flask import Blueprint, Response, request, current_app, json

android: flask.blueprints.Blueprint = Blueprint('android', __name__)


@android.route('/receive_string', methods=['POST'])
def receive_string() -> Response:
    data = request.get_json()
    if 'scanned_string' not in data:
        return current_app.response_class(
            response=json.dumps({'error': 'No string provided'}),
            status=400,
            mimetype='application/json'
        )

    hex_string = data['scanned_string']
    decoded_string = bytes.fromhex(hex_string).decode('utf-8')
    print(f"Received hex string: {hex_string}")
    print(f"Decoded string: {decoded_string}")

    return current_app.response_class(
        response=json.dumps({'success': 'String received successfully', 'decoded_string': decoded_string}),
        status=200,
        mimetype='application/json'
    )
