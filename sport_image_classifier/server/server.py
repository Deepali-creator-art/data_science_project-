
from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)

"""

Packages:
import numpy as np
import pywt
import cv2

import joblib
import json
import numpy as np
import base64
import cv2

from flask import Flask, request, jsonify
import util

pywavelets
scikitlearn
opencv2
numpy
flask

"""