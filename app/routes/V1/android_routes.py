import flask
from flask import Blueprint, Response, request, current_app, send_file, json, make_response

import io
import qrcode
from qrcode.main import QRCode

global_scanned_string = ""

android: flask.blueprints.Blueprint = Blueprint('android', __name__)


@android.route('/receive_string', methods=['POST'])
def receive_string() -> Response:
    global global_scanned_string

    data = request.get_json()
    if 'scanned_string' not in data:
        return current_app.response_class(
            response=json.dumps({'error': 'No string provided'}),
            status=400,
            mimetype='application/json'
        )

    try:
        scanned_string = data['scanned_string']
    except ValueError as e:
        return current_app.response_class(
            response=json.dumps({'error': 'Invalid string'}),
            status=400,
            mimetype='application/json'
        )

    global_scanned_string = scanned_string
    print(f"Received string: {scanned_string}")

    return current_app.response_class(
        response=json.dumps({'success': 'String received successfully', 'string': scanned_string}),
        status=200,
        mimetype='application/json'
    )


@android.route('/generate_qr', methods=['GET'])
def generate_qr_code() -> Response:
    global global_scanned_string

    if not global_scanned_string:
        return current_app.response_class(
            response=json.dumps({'error': 'No string available to generate QR code'}),
            status=400,
            mimetype='application/json'
        )

    qr = QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(global_scanned_string)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr)
    img_byte_arr.seek(0)

    response = make_response(send_file(img_byte_arr, mimetype='image/png'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response
