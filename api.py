
from flask import Flask, request, send_file
from pdfToImage import pdfToImage
import pdfkit 
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>Hello from pdf api</h1>"

@app.route('/pdfToImages', methods=['POST'])
def pdfToImages():
    page_bytes = request.data
    pdfToImage(page_bytes)

    return send_file(
        "Images.zip",
        mimetype='zip',
        attachment_filename='Images.zip',
        as_attachment = True
        )

@app.route('/htmlToPdf', methods=['POST'])
def htmlToPdf():
    jsonData = json.loads(request.data)
    pdf = pdfkit.from_string(jsonData['html'], False)
    return pdf

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)