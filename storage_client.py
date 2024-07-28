from flask import Flask, request, jsonify, session
import requests
import os


app = Flask(__name__)
input('Please set the secret key in the source code', app.secret_key)
app.secret_key = 'your_secret_key'
BASE_URL = os.getenv('API_BASE_URL', 'http://127.0.0.1:5000')
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your_default_secret_key')

def register(username, password):
    register_url = f'{BASE_URL}/register'
    register_data = {'username': username, 'password': password}
    response = requests.post(register_url, data=register_data)
    return response.text

def login(username, password):
    login_url = f'{BASE_URL}/login'
    login_data = {'username': username, 'password': password}
    response = requests.post(login_url, data=login_data)
    session_cookie = response.cookies.get('session')
    return session_cookie

def generate_api_key(session_cookie):
    generate_key_url = f'{BASE_URL}/generate-key'
    headers = {'Cookie': f'session={session_cookie}'}
    response = requests.post(generate_key_url, headers=headers)
    api_key = response.json().get('api_key')
    return api_key

def upload_file(api_key, file_path):
    upload_url = f'{BASE_URL}/upload'
    files = {'file': open(file_path, 'rb')}
    headers = {'API-Key': api_key}
    response = requests.post(upload_url, files=files, headers=headers)
    upload_result = response.json()
    return upload_result

def download_file(filename):
    file_url = f'{BASE_URL}/files/{filename}'
    response = requests.get(file_url)
    return response.content

@app.route('/generate-key', methods=['POST'])
def generate_key_endpoint():
    if 'username' not in session:
        return jsonify({'error': 'Unauthorized access'}), 403
    session_cookie = login(session['username'], session['password'])
    api_key = generate_api_key(session_cookie)
    return jsonify({'api_key': api_key})

@app.route('/upload', methods=['POST'])
def upload_file_endpoint():
    api_key = request.headers.get('API-Key')
    file = request.files['file']
    file_path = f"/path/to/save/{file.filename}"
    file.save(file_path)
    upload_result = upload_file(api_key, file_path)
    return jsonify(upload_result)

if __name__ == "__main__":
    app.run(debug=True)
