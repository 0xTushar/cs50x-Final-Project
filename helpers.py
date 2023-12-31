from flask import g, jsonify, request
from functools import wraps
import os
from werkzeug.utils import secure_filename
import hashlib
import uuid


def check_pdf_upload(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.method == 'POST':
            # Check if the post request has the file part
            if 'pdf' not in request.files:
                return jsonify({'error': 'No PDF file part'}), 400

            pdf = request.files['pdf']

            # If the user does not select a file, the browser submits an empty file without a filename
            if pdf.filename == '':
                return jsonify({'error': 'No PDF file part'}), 400

            # If the file is present and has a valid filename
            if pdf and pdf.filename.endswith(".pdf"):
                filename = secure_filename(pdf.filename)
                random = str(uuid.uuid4().hex)
                temp = os.path.join('uploads', f'{random}_{filename}')
                pdf.save(temp)
                random = calculate_file_hash(temp, 'md5')
                pdf_location = os.path.join('uploads', f'{random}_{filename}')
                os.rename(temp, pdf_location)
                # Store the file location in the 'g' object, which is available for the duration of the request
                g.pdf = pdf_location
                g.file_id = random
        return f(*args, **kwargs)
    return decorated_function


def calculate_file_hash(file_path, hash_algorithm):
    # Initialize the hash object for the specified algorithm
    hasher = hashlib.new(hash_algorithm)

    # Read the file in chunks and update the hash
    with open(file_path, 'rb') as file:
        while True:
            chunk = file.read(8192)  # Read in 8KB chunks
            if not chunk:
                break
            hasher.update(chunk)

    # Return the hexadecimal representation of the hash
    return hasher.hexdigest()
