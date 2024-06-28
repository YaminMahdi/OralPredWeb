import base64
import os

import numpy as np
import tensorflow as tf
from keras.optimizers import Adamax
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
imagePath = ""
image_b64 = ""
model = tf.keras.models.load_model("oral-efficientNet.h5", compile=False)
model.compile(Adamax(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

classes = ['Normal', 'Oral Cancer']


@app.route('/prediction')
def predict_model():
    img = image.load_img(imagePath, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    predict = model.predict(img_array)
    accuracy = max([item for sublist in predict for item in sublist])
    acc_per = "{:.2f}".format(accuracy*100)+"%"
    print(predict)
    predicted_class_index = np.argmax(predict)

    predicted_class = classes[predicted_class_index]
    print(imagePath, ": ", predicted_class)
    return {
        "accuracy": acc_per,
        "class": predicted_class
    }
    # return render_template('index.html', image=image_b64, prediction=predicted_class)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        global imagePath
        global image_b64
        img = request.files['image']
        if not os.path.exists("test_img"):
            os.makedirs("test_img")
        imagePath = os.path.join("test_img", secure_filename(img.filename))
        img.save(imagePath)
        with open(imagePath, "rb") as img_file:
            img_bytes = base64.b64encode(img_file.read())
        image_b64 = img_bytes.decode('utf-8')
        return render_template('index.html', image=image_b64)
    return render_template('index.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
