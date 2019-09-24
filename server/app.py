#! env/bin/python3
from os import path
import sys
from flask import Flask, jsonify, request, send_file
import uuid
import cv2
import numpy as np
import matplotlib.pyplot as plt

modulePath = path.abspath(path.join(path.dirname(__file__), '../'))
sys.path.append(modulePath)

from modules import skin_detection, convert
from helpers import upload, error

app = Flask(__name__)

uploadPath = path.join(path.dirname(__file__), 'uploads/')
transformedPath = path.join(path.dirname(__file__), 'transformed/')
app.config['UPLOAD_FOLDER'] = uploadPath

@app.route('/skin', methods=['POST'])
@error.error_handler
@upload.transform_upload(uploadPath, transformedPath, request, skin_detection.get_skin)
def skinDetection(*args, **kwargs):
  return jsonify({ "status": "sucess", "image": f"{request.host_url}image/{args[0]}" })

@app.route('/gray', methods=['POST'])
@error.error_handler
@upload.transform_upload(uploadPath, transformedPath, request, convert.gray2color)
def grayConversion(image): 
  return jsonify({ "status": "sucess", "image": f"{request.host_url}image/{image}" })

@app.route('/image/<image_name>', methods=['GET'])
@error.error_handler
def imageQuery(image_name): 
  return send_file(f"{transformedPath}{image_name}")

if __name__ == '__main__':
   app.run(port=3000, debug=True)