from datetime import datetime, timezone

import flask
from flask import Blueprint, Response, request, current_app, send_file, json, make_response

import io
import qrcode
from qrcode.main import QRCode

from app.database.enums import SurfaceType, WorkerType
from app.database import TableTopPattern
from app.services import TableTopService, ColorPalletService, TableTopPatternService, ColorPalletPatternService, \
    path_to_base64, role_required, process_image, get_similar_id, decode_image, convert_image_to_base64, format_data, \
    save_image, process_image_pattern
from app.services.parse_color import colors_to_hex_list

global_scanned_string = ""

android: flask.blueprints.Blueprint = Blueprint('android', __name__)


# дописать логику для сканирования и сохранения боковой части столешницы (паттерн)
@android.route('/add_pattern', methods=["POST"], endpoint='add_pattern')
def add_pattern() -> Response:
    data = request.json
    main_image_base64 = data.get("main_image", None)
    side_image_base64 = data.get("side_image", None)

    if main_image_base64 is None or side_image_base64 is None:
        return current_app.response_class(
            response=json.dumps({
                'msg': 'No image provided'
            }),
            status=400,
            mimetype='application/json'
        )

    try:
        img, perimeter, width, height, colors, img_path = process_image_pattern(main_image_base64)
        img_base64 = convert_image_to_base64(img)

        tt_id = TableTopPatternService.insert_top_pattern(
            width,
            height,
            perimeter,
            img_path
        )

        success = ColorPalletPatternService.insert_all_cpp(SurfaceType.MAIN.value, colors, tt_id)

        colors_list = colors_to_hex_list(colors)

        if success:
            return current_app.response_class(
                response=json.dumps({
                    'msg': 'success',
                    'imgBase64': img_base64,
                    'perimeter': perimeter,
                    'width': width,
                    'height': height,
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


# дописать логику для сканирования и поиска по боковой части столешницы
@android.route('/find_pattern', methods=["POST"], endpoint='find_pattern')
def find_pattern() -> Response:
    data = request.json
    main_image_base64 = data.get("main_image", None)
    side_image_base64 = data.get("side_image", None)

    if main_image_base64 is None or side_image_base64 is None:
        return current_app.response_class(
            response=json.dumps({
                'msg': 'No image provided'
            }),
            status=400,
            mimetype='application/json'
        )

    try:
        img, perimeter, width, height, colors = process_image(main_image_base64)

        ttp_id = get_similar_id(width, height, perimeter, colors, 0.1)

        if ttp_id is None:
            return current_app.response_class(
                response=json.dumps({
                    'msg': 'No pattern with this parameters'
                }),
                status=400,
                mimetype='application/json'
            )

        print(ttp_id)

        pattern: TableTopPattern | None = TableTopPatternService.get_top_pattern(ttp_id)

        return current_app.response_class(
            response=json.dumps({
                'msg': 'Table top successfully find',
                'pattern_id': ttp_id,
                'article': pattern.article,
                'name': pattern.name,
                'material': pattern.material,
                'pattern_width': pattern.width,
                'pattern_height': pattern.height,
                'pattern_perimeter': pattern.perimeter,
                'pattern_depth': pattern.depth,
                'pattern_image_base64': path_to_base64(pattern.image_path),
                'perimeter': perimeter,
                'width': width,
                'height': height,
                'colors': format_data(colors, 60),
                'image_base64': main_image_base64
            }),
            status=200,
            mimetype='application/json'
        )

    except Exception as e:
        print(f"Exception occurred: {e}")
        return current_app.response_class(
            response=json.dumps({
                'msg': 'An error occurred during processing'
            }),
            status=500,
            mimetype='application/json'
        )


# подлежит удалению
@android.route('/processing_cv', methods=["POST"])
def processing_cv() -> Response:
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

        ttp_id = get_similar_id(width, height, perimeter, colors, 0.1)
        print(ttp_id)

        tt_id = TableTopService.insert_top(
            int(datetime.now(timezone.utc).timestamp() * 1000),
            width,
            height,
            perimeter,
            img_path,
            ttp_id
        )

        success = ColorPalletService.insert_all_cp(SurfaceType.MAIN.value, colors, tt_id)

        cnt_list = format_data(cnt, 3)

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
