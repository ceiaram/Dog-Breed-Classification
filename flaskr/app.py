from flask import Flask, jsonify
from flask import Flask, render_template, request, redirect
import os

from prediction import get_prediction


app = Flask(__name__)


# import requests

# resp = requests.post("http://localhost:5000/predict",
#                      files={"file": open('./_static/img/winston.jpg','rb')})

@app.route("/")
def index():
        return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files.get('file')
        if not file:
            return
        img_bytes = file.read()
        prediction = get_prediction(image_bytes=img_bytes)
        # class_id, class_name = get_prediction(image_bytes=img_bytes)
        # class_name = format_class_name(class_name)
        # return render_template('result.html', class_id=class_id,
        #                        class_name=class_name)
        return render_template('result.html', prediction)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
