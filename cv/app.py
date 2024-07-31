from flask import Flask, render_template, request, redirect
import numpy as np
import cv2
import utils
import base64

app = Flask(__name__)


@app.route('/')
def form():
    return render_template("form.html")


@app.route('/out', methods=["POST"])
def output():
    image = request.files.get("image", None)
    if image is None:
        return redirect("/")

    file_bytes = np.fromfile(image, np.uint8)
    file = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    img, cnt, colors = utils.produce_contours(file, draw_contours=True)
    _, bs64 = cv2.imencode(f".{image.filename.split('.')[-1]}", img)

    return render_template(
        "output.html",
        imgBase64=base64.b64encode(bs64).decode(),
        contours=cnt[:3],
        colors=colors[:7],
    )


if __name__ == '__main__':
    app.run(debug=True)
