from flask import Flask, request, send_from_directory, abort
import os
import json

app = Flask(__name__)

# Directory where the libraries and frameworks are stored
LIBS_DIR = "./server/items/libs"
FRAMEWORKS_DIR = "./server/items/frameworks"

# Example username and password (for demo purposes, use more secure methods in production)
USERS = {
    "user": "password"
}

# Configuration file paths
LIBS_CONF_FILE = os.path.join(LIBS_DIR, 'conf.json')
FRAMEWORKS_CONF_FILE = os.path.join(FRAMEWORKS_DIR, 'conf.json')

# Ensure the directories exist
os.makedirs(LIBS_DIR, exist_ok=True)
os.makedirs(FRAMEWORKS_DIR, exist_ok=True)

# Function to read config file
def read_config(conf_file):
    if os.path.exists(conf_file):
        with open(conf_file, 'r') as f:
            return json.load(f)
    return {"files": {}}

# Manual authentication function
def authenticate(username, password):
    if username in USERS and USERS[username] == password:
        return True
    return False

# Route for uploading a file (push operation)
@app.route('/push', methods=['POST'])
def push_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(LIBS_DIR, filename)
    try:
        file.save(file_path)

        # Update password in conf.json if provided
        password = request.form.get('password', '')
        if password:
            update_password(filename, password)

        return f"File {filename} uploaded successfully", 200
    except Exception as e:
        print(e)
        return "File upload failed", 500

# Route for pulling a file (pull operation)
@app.route('/pull/<path:filename>', methods=['GET'])
def pull_file(filename):
    try:
        # Ensure the requested file is within the LIBS_DIR or FRAMEWORKS_DIR
        if os.path.exists(os.path.join(LIBS_DIR, filename)):
            dir_path = LIBS_DIR
        elif os.path.exists(os.path.join(FRAMEWORKS_DIR, filename)):
            dir_path = FRAMEWORKS_DIR
        else:
            abort(404)

        # Check if file is password protected
        if is_password_protected(filename, dir_path):
            # Check if the provided auth token matches the password
            auth_token = request.headers.get('Authorization')
            password = get_password(filename, dir_path)
            if not auth_token or auth_token != password:
                return "Unauthorized", 401

        return send_from_directory(dir_path, filename, as_attachment=True)
    except Exception as e:
        print(e)
        abort(500)

# Function to update password in conf.json
def update_password(filename, password):
    conf_file = LIBS_CONF_FILE if os.path.exists(os.path.join(LIBS_DIR, filename)) else FRAMEWORKS_CONF_FILE
    config = read_config(conf_file)
    config['files'][filename] = password
    write_config(conf_file, config)

# Function to get password from conf.json
def get_password(filename, dir_path):
    conf_file = LIBS_CONF_FILE if dir_path == LIBS_DIR else FRAMEWORKS_CONF_FILE
    config = read_config(conf_file)
    return config['files'].get(filename, "")

# Function to check if file is password protected
def is_password_protected(filename, dir_path):
    conf_file = LIBS_CONF_FILE if dir_path == LIBS_DIR else FRAMEWORKS_CONF_FILE
    config = read_config(conf_file)
    return filename in config['files'] and config['files'][filename] != ""

if __name__ == '__main__':
    app.run(debug=True, port=5000)
