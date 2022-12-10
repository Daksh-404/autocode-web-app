#  importing important libraries
from flask import Flask
import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import sys
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

path = '/'

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
            path =(os.path.join(app.config['UPLOAD_FOLDER'], "uploads", filename))     
            file.save(path)
            if request.form["action"] == "gui_to_code":
                return redirect('/gui')   
            elif request.form["action"] == "wireframe_to_code":
                return redirect('/wireframe') 
	    	    
    return render_template('index.html')

@app.route('/gui', methods=['GET'])
def gui_to_code():
    
    return render_template('gui.html')

@app.route('/wireframe', methods=['GET'])
def wireframe_to_code():
    
    return render_template('wireframe.html')
    
# for showing image frames, videos and the captions
# @app.route('/out', methods=['POST', 'GET'])
# def out():
# 	#running the batch file
# 	if request.method == "POST":
# 		subprocess.call([r'test.bat'])
	
# 	#setting up the captions
# 	caps = ["The man is riding a bicycle", "The man is on a bike", "The man is high and floating"]
 
# 	# setting up the main image path
# 	path_to_image = "/Users/daksh_mac/Desktop/everything/Dev/gitRepos/HELIX/helix-web-app/helix/templates/sample.jpg"
# 	return render_template('soft.html', ca = caps, path = path_to_image)

if __name__ == "__main__" :
	app.run(debug = True, port = 8000)