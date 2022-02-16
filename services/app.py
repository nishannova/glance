#app.py
from flask import Flask, flash, request, redirect, url_for, render_template
import urllib.request
import os
from werkzeug.utils import secure_filename
from loguru import logger
import sys
sys.path.append('/Users/sali115/image_scan/src')
from main import *
# from ui import demo_ui

app = Flask(__name__)
 
UPLOAD_FOLDER = 'static/uploads'
 
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
     
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload_image():
    barcode_dtls = dict()

    barcode_type=selected = str(request.form.get("barcode_type"))
    logger.warning(f"Uploading Image: TYPE:{barcode_type}")
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #print('upload_image filename: ' + filename)
        flash('Image successfully uploaded and displayed below')
        barcode_dtls = process_doc(file_path=os.path.join('/Users/sali115/image_scan/services/static/uploads'), save=False, ui=True, barcode_type=barcode_type)
        logger.warning(f"BARCODE DETAILS: {barcode_dtls}")
        return render_template('index.html', filename=filename, barcode_dtls=barcode_dtls[filename])
    else:
        flash('Allowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
 
@app.route('/display/<filename>')
def display_image(filename):
    logger.warning(f"Trying to display {filename}")
    return redirect(url_for('static', filename='uploads/' + filename), code=301)
 
if __name__ == "__main__":
    app.run(debug=True)