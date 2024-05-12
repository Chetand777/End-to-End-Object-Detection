import sys, os
import cv2, shutil
import numpy as np
import logging, subprocess
from signlanguage.pipeline.training_pipeline import TrainingPipeline
from signlanguage.exception import SignException
from signlanguage.utils.main_utils import decodeImage, encodeImageintoBase64
from flask_cors import CORS, cross_origin
from flask import Flask, request, jsonify, render_template, Response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

class ClientApp:
  def __init__(self):
    self.filename = "inputImage.jpg"

@app.route('/')
def home():
  return render_template('index.html')

@app.route("/train")
def trainroute():
  obj = TrainingPipeline()
  obj.run_pipeline()
  logger.info("Training Successful!!")
  return "Training Successful!!"

@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predictroute(): 
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)
        logger.info("Image decoded successfully.")

        # Execute YOLOv5 prediction using subprocess
        command = "cd yolov5 && python detect.py --weights best.pt --img 416 --conf 0.5 --source ../data/inputImage.jpg"
        subprocess.run(command, shell=True)
        logger.info("Prediction completed.")

        # Encode predicted image to base64
        opencodedbase64 = encodeImageintoBase64("yolov5/runs/detect/exp/inputImage.jpg")
        logger.info("Image encoded to base64.")

        result = {'Image': opencodedbase64.decode('utf-8')}

        # Remove temporary files
        shutil.rmtree('yolov5/runs')
        logger.info("Temporary files removed.")

    except ValueError as val:
        logger.error(val)
        return Response('Value not found inside json data')
    except KeyError:
        logger.error('Key value error incorrect key passed')
        return Response('Key value error incorrect key passed')
    except Exception as e:
        logger.error(e)
        result = 'Invalid Input'

    return jsonify(result)


@app.route("/live", methods=['GET'])
@cross_origin()
def predictlive():
  try:
    os.system("cd yolov5 & python detect.py --weights best.pt --img 416 --conf 0.5 --source 0")
    logger.info("Live prediction started.")
    os.remove('yolov5/runs')
    logger.info("Temporary files removed.")
    return "Camera starting"
  except ValueError as val:
    logger.error(val)
    return Response('Value not found inside json data')

if __name__ == "__main__":
  clApp = ClientApp()
  app.run(host='0.0.0.0', port=8080)
