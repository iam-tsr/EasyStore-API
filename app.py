from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, send_from_directory
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import uuid
import json
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

STORAGE_FILE = 'storage.json'

def initialize_storage():
    if not os.path.exists(STORAGE_FILE) or os.path.getsize(STORAGE_FILE) == 0:
        with open(STORAGE_FILE, 'w') as f:
            json.dump({'users': {}, 'keys': {}}, f)

def load_storage():
    with open(STORAGE_FILE, 'r') as f:
        storage = json.load(f)
        if 'users' not in storage:
            storage['users'] = {}
        if 'keys' not in storage:
            storage['keys'] = {}
        return storage

def save_storage(data):
    with open(STORAGE_FILE, 'w') as f:
        json.dump(data, f, indent=4)

class User(UserMixin):
    def __init__(self, id, username):
        self.id = id
        self.username = username

@login_manager.user_loader
def load_user(user_id):
    storage = load_storage()
    if user_id in storage['users']:
        user_data = storage['users'][user_id]
        return User(user_id, user_data['username'])
    return None

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        storage = load_storage()
        for user_id, user_data in storage['users'].items():
            if user_data['username'] == username and check_password_hash(user_data['password'], password):
                user = User(user_id, username)
                login_user(user)
                return redirect(url_for('index'))
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        storage = load_storage()
        user_id = str(uuid.uuid4())
        storage['users'][user_id] = {'username': username, 'password': hashed_password}
        save_storage(storage)
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/generate', methods=['POST'])
@login_required
def generate_key():
    description = request.form['description']
    new_key = str(uuid.uuid4())
    storage = load_storage()
    storage['keys'][new_key] = {'description': description, 'active': True}
    save_storage(storage)
    return redirect(url_for('index'))

@app.route('/keys', methods=['GET'])
@login_required
def list_keys():
    storage = load_storage()
    return jsonify(storage['keys'])

if __name__ == '__main__':
    initialize_storage()
    app.run(debug=True)
