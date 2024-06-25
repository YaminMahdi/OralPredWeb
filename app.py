import base64

from flask import Flask, render_template, request

app = Flask(__name__)

image = ""


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        global image
        image = request.files['image']
        image_b64 = base64.b64encode(image.read()).decode('utf-8')
        return render_template('index.html', image=image_b64)
    return render_template('index.html')


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
