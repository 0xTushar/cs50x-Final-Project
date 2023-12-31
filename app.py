import os
from flask import Flask, render_template, request, jsonify, g, send_from_directory
from helpers import check_pdf_upload
import fitz  # PyMuPDF

# configure application
app = Flask(__name__)


@app.after_request
def after_request(response):
    """Ensure file is deleted"""
    pdf_file = getattr(g, 'pdf', None)
    if pdf_file:
        os.remove(pdf_file)
    return response


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/extract-pdf-text", methods=["GET", "POST"])
@check_pdf_upload
def text():
    if request.method == "POST":
        pdf_file = getattr(g, 'pdf', None)
        pdf = fitz.open(pdf_file)
        plain_text = ""
        for page in pdf:
            plain_text += page.get_text()
        pdf.close()
        output = f"users/{getattr(g, 'file_id', 'example')}.txt"
        with open(output, 'w', encoding='utf-8') as file:
            file.write(plain_text)

        return jsonify({'file': output}), 200

    else:
        return render_template('text.html')


@app.route("/extract-pdf-images", methods=["GET", "POST"])
@check_pdf_upload
def images():
    if request.method == "POST":
        pdf_file = getattr(g, 'pdf', None)
        pdf = fitz.open(pdf_file)
        for page_index in range(len(pdf)):  # iterate over pdf pages
            page = pdf[page_index]  # get the page
            image_list = page.get_images()

            # print the number of images found on the page
            if image_list:
                print(f"Found {len(image_list)} images on page {page_index}")
            else:
                print("No images found on page", page_index)
            images = []
            # enumerate the image list
            for image_index, img in enumerate(image_list, start=1):
                xref = img[0]  # get the XREF of the image
                pix = fitz.Pixmap(pdf, xref)  # create a Pixmap

                if pix.n - pix.alpha > 3:  # CMYK: convert to RGB first
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                output = f"users/{getattr(g, 'file_id', 'example')}-"
                image = f"{output}page_{page_index}-image_{image_index}.png"
                pix.save(image)  # save the image as png
                images.append(image)
                pix = None

        return jsonify({'images': images}), 200
    else:
        return render_template('images.html')


@app.route("/merge-pdf", methods=["GET", "POST"])
@check_pdf_upload
def merge():
    if request.method == "POST":
        pdf_file = getattr(g, 'pdf', None)
        return ""
    else:
        return render_template('merge.html')


@app.route("/ocr-pdf", methods=["GET", "POST"])
@check_pdf_upload
def ocr():
    if request.method == "POST":
        pdf_file = getattr(g, 'pdf', None)
        return ""
    else:
        return render_template('ocr.html')


# Function to calculate the hash of a file using a specific hash algorithm


@app.route('/users/<filename>')
def uploaded_file(filename):
    return send_from_directory('users', filename)


if __name__ == '__main__':
    app.run(debug=True)