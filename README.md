# PDF Tools Online

#### Video Demo: https://youtu.be/xSTvBe8wGNw

#### Description:
Welcome to **PDF Tools Online**, a user-friendly and free-to-use online platform offering a suite of PDF tools designed to enhance your productivity. This web application, built using the Flask framework, provides a seamless experience for performing various operations on PDF files.


![Free and easy-to-use online PDF tools that make you more productive](https://github.com/0xTushar/cs50x-Final-Project/assets/55528085/69f085bf-9c9e-435c-8926-61dc0696ed3c)



### Features
1. **Extract Text from PDF:**
   - Effortlessly convert PDFs to text.
   - Boost productivity with the PDF Text Extractor.
   - No cumbersome installation process.
   ![Extract Text from PDF](https://github.com/0xTushar/cs50x-Final-Project/assets/55528085/42853b22-3401-46ee-aaeb-1c52e09492e4)

2. **Extract Images from PDF:**
   - Retrieve all images from your PDF documents instantly.
   - Maintain image quality throughout the extraction process.
   - Preview extracted images.

   ![Extract Images from PDF](https://github.com/0xTushar/cs50x-Final-Project/assets/55528085/25e37a2e-c666-4a40-9430-9f81fd041fbc)

3. **Merge PDF:**
   - Merge multiple PDF files into one.
   - Secure and easy-to-use PDF merger.
   - Safely combine PDF files with ease.

   ![Merge PDF](https://github.com/0xTushar/cs50x-Final-Project/assets/55528085/3b315495-2b91-498d-b9e9-56f2569d57cf)

4. **PDF OCR (Optical Character Recognition):**
   - Extract text from scanned documents using OCR.
   - Compatible with any device and operating system.
   - Cloud-based solution for improved accessibility.

   ![PDF OCR](https://github.com/0xTushar/cs50x-Final-Project/assets/55528085/a5477fce-5258-4cd9-87ad-67e2d776cf4d)


## Getting Started

To run the application locally, follow these steps:

1. Install the required modules listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt

2. Run the Flask application.
    ```bash
    python app.py

3. Open your browser and navigate to `http://localhost:5000` to access the PDF Tools Online.
     Feel free to explore and utilize the various PDF tools offered by the platform. For more details, refer to the video demo.

Enjoy using PDF Tools Online!


### Project Structure

- **./templates:** Contains HTML files for different views, such as text extraction, image extraction, OCR, and merging.

- **./static:** Holds the PDF tool sprite in SVG format and the CSS styles (style.css).

- **./uploads:** The directory where user-uploaded files are stored.

- **helpers.py:** Module containing upload helpers and file hash calculation helpers.

- **requirements.txt:** Lists all the required Python modules.

- **app.py:** The main entry point for the application.

- **README.md:** Detailed information about the project.

## ./templates

This directory contains HTML files for different views within the PDF Tools Online web application. Each HTML file corresponds to a specific functionality:

- **index.html:** Root landing page.
- **text.html:** View for extracting text from PDF.
- **images.html:** View for extracting images from PDF.
- **merge.html:** View for merging multiple PDF files.
- **ocr.html:** View for performing OCR on scanned PDFs.
- **layout.html:** Common layout file used across views.

## ./static

The `static` directory houses static assets, such as stylesheets and images, required for the web application:

- **style.css:** CSS styles for styling the user interface.
- **pdf-tool-sprite.svg:** SVG sprite used for icons and graphics.

## ./uploads

This directory is where user-uploaded files are stored temporarily during the operation of the PDF Tools Online application.

## helpers.py

The `helpers.py` file contains utility functions that assist in various aspects of the web application:

- **Upload Helpers:** Functions for handling file uploads.
- **Hash Calculation Helpers:** Functions for calculating file hashes.

## ./requirements.txt

This file lists all the required Python modules and their versions. It ensures that the necessary dependencies are installed when setting up the project.

## app.py

The `app.py` file serves as the main entry point for the PDF Tools Online application. It initializes the Flask web server and defines the routes and functionality for each view.

## README.md

The `README.md` file is a comprehensive document that provides an overview of the project, details about its features, the project structure, and instructions on how to run the application locally.


