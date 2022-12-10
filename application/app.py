#  importing important libraries
from flask import Flask
import os
from flask import Flask, request, redirect, url_for, render_template, session
import json
from werkzeug.utils import secure_filename
import sys
from autocode.predict_gui import *
from autocode.predict_wireframe import *
from PIL import Image

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) 

ALLOWED_EXTENSIONS = {'jpg', 'jpeg','png','JPG','JPEG','PNG'}

app = Flask(__name__, template_folder='./templates', static_folder='./static')
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# limit upload size upto 8mb
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

image_path = '/'

# landing page
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = (os.path.join(app.config['UPLOAD_FOLDER'], "static/uploads", filename))  
            image_path = path   
            file.save(path)
            if request.form["action"] == "gui_to_code":
                return redirect(url_for('.gui_to_code', img_path=path))   
            elif request.form["action"] == "wireframe_to_code":
                return redirect('/wireframe') 
	    	    
    return render_template('index.html')

# code generated from GUI
@app.route('/gui', methods=['GET'])
def gui_to_code():  
    img_path = request.args['img_path']
    img_name = img_path.split("/")[-1:][0]
    final_img_path = "static/uploads/" + img_name   
    code = predict_gui(img_path)
    return render_template('code.html', img_path=final_img_path, code=code)

# code generated from Wireframe or Sketch
@app.route('/wireframe', methods=['GET'])
def wireframe_to_code():
    code = predict_wireframe(image_path)
    return render_template('code.html', img_path=image_path, code=code)
    

if __name__ == "__main__" :
	app.run(debug = True, port = 8000)