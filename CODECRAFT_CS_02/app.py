from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
import os
from PIL import Image
import numpy as np
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'change_this_secret'

# Folder configuration
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def xor_process(input_path, output_path, key):
    img = Image.open(input_path).convert('RGB')
    arr = np.array(img)
    flat = arr.flatten()
    key_bytes = bytearray(key.encode())

    for i in range(len(flat)):
        flat[i] ^= key_bytes[i % len(key_bytes)]

    encrypted_arr = flat.reshape(arr.shape)
    Image.fromarray(encrypted_arr).save(output_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    original = encrypted = decrypted = None

    if request.method == 'POST':
        file = request.files.get('file')
        key = request.form.get('key')
        action = request.form.get('action')

        if not file or not allowed_file(file.filename) or not key:
            flash("Please upload a valid image and enter a password.")
            return redirect(url_for('index'))

        filename = secure_filename(file.filename)
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)
        original = filename

        if action == 'encrypt':
            encrypted = 'enc_' + filename
            xor_process(upload_path, os.path.join(app.config['PROCESSED_FOLDER'], encrypted), key)

        elif action == 'decrypt':
            decrypted = 'dec_' + filename
            xor_process(upload_path, os.path.join(app.config['PROCESSED_FOLDER'], decrypted), key)

    return render_template('index.html', original=original, encrypted=encrypted, decrypted=decrypted)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/processed/<filename>')
def processed_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
