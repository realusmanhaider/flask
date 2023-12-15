from flask import Flask, request, send_file
import rembg
from io import BytesIO

app = Flask(__name__)


def remove_background(input_data):
    output_data = rembg.remove(input_data)
    return BytesIO(output_data)


@app.route('/remove_background', methods=['POST'])
def remove_background_api():
    if 'file' not in request.files:
        return 'No file part in the request', 400

    file = request.files['file']

    if file.filename == '':
        return 'No selected file', 400

    if file:
        try:
            input_data = file.read()
            output_image = remove_background(input_data)
            return send_file(output_image, mimetype='image/png')
        except Exception as e:
            return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)
