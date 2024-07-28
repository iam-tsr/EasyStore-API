from flask import Flask, request, jsonify, send_from_directory
import os
import uuid
import json

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create the upload directory if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load existing API keys and storage information
if os.path.exists('storage.json'):
    with open('storage.json', 'r') as f:
        storage_data = json.load(f)
else:
    storage_data = {}

def save_storage_data():
    with open('storage.json', 'w') as f:
        json.dump(storage_data, f)

@app.route('/generate-key', methods=['POST'])
def generate_key():
    api_key = str(uuid.uuid4())
    storage_data[api_key] = []
    save_storage_data()
    return jsonify({'api_key': api_key})

@app.route('/upload', methods=['POST'])
def upload_file():
    api_key = request.headers.get('API-Key')
    if not api_key or api_key not in storage_data:
        return jsonify({'error': 'Invalid API Key'}), 403

    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected for uploading'}), 400

    filename = f"{uuid.uuid4()}_{file.filename}"
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    storage_data[api_key].append(filename)
    save_storage_data()

    return jsonify({'message': 'File successfully uploaded', 'filename': filename})

@app.route('/files/<filename>', methods=['GET'])
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
