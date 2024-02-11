from flask import Flask, jsonify
from flask import Flask, render_template, request, redirect
import os

from prediction import get_prediction


app = Flask(__name__)

# {% for key, value in result.items() %}

#   <tr>
#     <th>{{ key }}</th>
#     <td>{{ value }}</td>
#   </tr>

#   {% endfor %}

# import requests

# resp = requests.post("http://localhost:5000/predict",
#                      files={"file": open('./_static/img/winston.jpg','rb')})

@app.route("/")
def index():
        return render_template('index.html')

@app.route('/predict', methods=['POST'])
@app.route('/predict/<prediction>')
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return
        print(file)
        img_bytes = file.read()
        prediction = get_prediction(image_bytes=img_bytes)
        # class_id, class_name = get_prediction(image_bytes=img_bytes)
        # class_name = format_class_name(class_name)
        # return render_template('result.html', class_id=class_id,
        #                        class_name=class_name)
        return render_template('results.html', prediction=prediction)
    return render_template('index.html')


if __name__ == '__main__':
    # app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
    
    app.run(debug = True)