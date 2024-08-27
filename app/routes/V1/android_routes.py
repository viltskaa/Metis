from datetime import datetime, timezone

import flask
from flask import Blueprint, Response, request, current_app, send_file, json, make_response

import io
import qrcode
from qrcode.main import QRCode

from app.database.enums import SurfaceType
from app.services import TableTopService, ColorPalletService, TableTopPatternService, ColorPalletPatternService
from app.services.search_similar_algorithm import get_similar_id
from cv import decode_image, process_image, convert_image_to_base64, format_data, save_image, process_image_pattern

global_scanned_string = ""

android: flask.blueprints.Blueprint = Blueprint('android', __name__)


@android.route('/add_pattern', methods=["POST"])
def add_pattern():
    print('add_pattern')
    data = request.json
    image_base64 = data.get("image", None)

    if image_base64 is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No image provided'}),
            status=400,
            mimetype='application/json'
        )

    # return current_app.response_class(
    #     response=json.dumps({
    #         'imgBase64': "gjrelgjslkjgkljsdlkjsdlkf",
    #         'contours': [],
    #         'colors': [[0, 0, 0], [114, 76, 55]]
    #     }),
    #     status=200,
    #     mimetype='application/json'
    # )

    try:
        image = decode_image(image_base64)
        img, cnt, colors = process_image_pattern(image)
        img_base64 = convert_image_to_base64(img)
        img_path = save_image(image)

        perimeter, width, height = cnt[0]

        tt_id = TableTopPatternService.insert_top_pattern(
            width,
            height,
            perimeter,
            img_path
        )

        success = ColorPalletPatternService.insert_all_cpp(SurfaceType.main.value, colors, tt_id)

        cnt_list = format_data(cnt, 3)
        colors_list = format_data(colors, 60)

        if success:
            return current_app.response_class(
                response=json.dumps({
                    'imgBase64': img_base64,
                    'contours': cnt_list,
                    'colors': colors_list
                }),
                status=200,
                mimetype='application/json'
            )

    except Exception as e:
        print(f"Exception occurred: {e}")
        return current_app.response_class(
            response=json.dumps({'error': 'An error occurred during processing'}),
            status=500,
            mimetype='application/json'
        )


@android.route('/processing_cv', methods=["POST"])
def processing_cv():
    print("processing_cv")
    data = request.json
    image_base64 = data.get("image", None)

    if image_base64 is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No image provided'}),
            status=400,
            mimetype='application/json'
        )

    try:
        image = decode_image(image_base64)
        img, cnt, colors = process_image(image)
        img_base64 = convert_image_to_base64(img)
        img_path = save_image(image)

        perimeter, width, height = cnt[0]

        print(get_similar_id(width, height, perimeter, colors, 0.1))

        tt_id = TableTopService.insert_top(
            int(datetime.now(timezone.utc).timestamp() * 1000),
            width,
            height,
            perimeter,
            img_path
        )

        success = ColorPalletService.insert_all_cp(SurfaceType.main.value, colors, tt_id)

        cnt_list = format_data(cnt, 3)

        # colors_list = format_data(colors, 7)
        colors_list = [list(map(int, color)) for color in colors]

        if success:
            return current_app.response_class(
                response=json.dumps({'success': 'Data received successfully',
                                     'imgBase64': img_base64,
                                     'contours': cnt_list,
                                     'colors': colors_list}),
                status=200,
                mimetype='application/json'
            )

    except Exception as e:
        print(f"Exception occurred: {e.with_traceback()}")
        return current_app.response_class(
            response=json.dumps({'error': 'An error occurred during processing'}),
            status=500,
            mimetype='application/json'
        )


@android.route('/process_images', methods=["POST"])
def process_images():
    print("process_images")
    data = request.json
    main_image = data.get("main", None)
    side_image = data.get("side", None)

    if main_image is None or side_image is None:
        return current_app.response_class(
            response=json.dumps({'error': 'No images provided'}),
            status=400,
            mimetype='application/json'
        )

    try:
        image = decode_image(main_image)
        img, cnt, colors = process_image(image)
        img_base64 = convert_image_to_base64(img)
        img_path = save_image(image)

        perimeter, width, height = cnt[0]

        print(get_similar_id(width, height, perimeter, colors, 0.1))

        tt_id = TableTopService.insert_top(
            int(datetime.now(timezone.utc).timestamp() * 1000),
            width,
            height,
            perimeter,
            img_path
        )

        success = ColorPalletService.insert_all_cp(SurfaceType.main.value, colors, tt_id)

        cnt_list = format_data(cnt, 3)

        # colors_list = format_data(colors, 7)
        colors_list = [list(map(int, color)) for color in colors]

        if success:
            return current_app.response_class(
                response=json.dumps({'success': 'Data received successfully',
                                     'imgBase64': img_base64,
                                     'contours': cnt_list,
                                     'colors': colors_list}),
                status=200,
                mimetype='application/json'
            )

    except Exception as e:
        print(f"Exception occurred: {e.with_traceback()}")
        return current_app.response_class(
            response=json.dumps({'error': 'An error occurred during processing'}),
            status=500,
            mimetype='application/json'
        )


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
