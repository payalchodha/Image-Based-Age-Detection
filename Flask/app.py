from __future__ import division, print_function
# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
from tensorflow import keras



# Keras
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
from keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template,send_from_directory
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Model saved with Keras model.save()
MODEL_PATH = 'models/cnn_model.h5'

# Load your trained model
model = keras.models.load_model(MODEL_PATH)
model._make_predict_function()          # Necessary
print('Model loaded. Start serving...')

# You can also use pretrained model from Keras
# Check https://keras.io/applications/
#from keras.applications.resnet50 import ResNet50
#model = ResNet50(weights='imagenet')
#print('Model loaded. Check http://127.0.0.1:5000/')


def model_predict(img_path, model):
    img = image.load_img(img_path, grayscale = True,target_size=(64, 64))

    # Preprocessing the image
    # x = img.resize((64,64))
    # x = x.astype('float32')
    x = image.img_to_array(img)/255

    # x = np.true_divide(x, 255)
    # x = np.arange(12288).reshape(3,64,64 )

    # x= x.reshape((64,64,1))
    # x = x.reshape((64,64,1))
    x = np.expand_dims(x, axis=0)

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    # x = preprocess_input(x,mode='caffe')

    preds = model.predict(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['image']

        # Save the file to ./uploadsfile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filename = secure_filename(f.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
        f.save(file_path)
        # return render_template('show.html', filename=image)
        # return redirect(url_for('send_file',
        #                             filename=filename))
        # basepath = os.path.dirname(__file__)
        # file_path = os.path.join(
        #     basepath, 'uploads', secure_filename(f.filename))
        # f.save(file_path)
        #
        # Make prediction
        preds = model_predict(file_path, model)

        # Process your result for human
        print(preds)
        pred_class = preds.argmax(axis=-1)            # Simple argmax
        #pred_class = decode_predictions(preds, top=1)[0]   # ImageNet Decode
        result = str(pred_class[0])
        #result = str(pred_class[0][0][1])

                    # Convert to string
        if result == '0':
            return 'MIDDLE'
        if result == '1':
            return 'OLD'
        if result == '2':
            return 'YOUNG'

    return None

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)
if __name__ == '__main__':
    app.run(port=5002, debug=True)

    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
