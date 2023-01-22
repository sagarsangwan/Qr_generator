QR Code Generator
This is a simple Flask app that generates a QR code image of a provided link.

Requirements
Python 3.x
Flask
qrcode
Installation
Clone the repository to your local machine


Install the required packages using the command
pip install -r requirements.txt

Start the Flask development server by running the command
flask run

Open a web browser and navigate to http://localhost:5000/?link=<your_link> to generate a QR code image of the provided link.

The QR code image will be saved as qr.png in the project directory.
This code saves the QR image with the name 'qr.png' in the same directory where the code is running.
If you want to save the image with different name or location please change the code accordingly
Please make sure that the provided link is a valid url.