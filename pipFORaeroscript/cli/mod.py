import os
import requests
import json

API_URL = "http://127.0.0.1:5000/"
LIBS_DIR = "./cli/aeromod"
FRAMEWORKS_DIR = "./cli/frameworks"
LIBS_CONF_FILE = "./server/items/libs/conf.json"
FRAMEWORKS_CONF_FILE = "./server/items/frameworks/conf.json"
CHUNK_SIZE = 1024 * 1024  # 1 MB chunk size for reading/writing


def read_config(conf_file):
    if os.path.exists(conf_file):
        with open(conf_file, 'r') as f:
            return json.load(f)
    return {"files": {}}


def write_config(conf_file, config):
    with open(conf_file, 'w') as f:
        json.dump(config, f, indent=4)


def push_file(file_path, password):
    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        response = requests.post(
            API_URL + 'push',
            files={'file': (file_name, f)},
            data={'password': password},
            headers={'Authorization': password} if password else None
        )
    if response.status_code == 200:
        print(f"File {file_name} uploaded successfully")
    else:
        print(f"Failed to upload file: {response.status_code} {response.text}")


def pull_file(filename, auth_token):
    url = f"http://localhost:5000/pull/{filename}"
    headers = {'Authorization': auth_token} if auth_token else None
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"File {filename} downloaded successfully")
    else:
        print(f"Error downloading {filename}: {response.status_code} {response.text}")


def push_framework(dir_path, password):
    for root, _, files in os.walk(dir_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            relative_path = os.path.relpath(file_path, dir_path)
            with open(file_path, 'rb') as f:
                response = requests.post(
                    API_URL + 'push-framework',
                    files={'file': (file_name, f)},
                    data={'path': relative_path, 'password': password},
                    headers={'Authorization': password} if password else None
                )
            if response.status_code == 200:
                print(f"File {relative_path} uploaded successfully")
            else:
                print(f"Failed to upload file {relative_path}: {response.status_code} {response.text}")


def pull_framework(dir_name, auth_token):
    response = requests.get(
        API_URL + 'pull-framework-dir/' + dir_name,
        headers={'Authorization': auth_token} if auth_token else None
    )
    if response.status_code == 200:
        file_list = response.json()
        for file_name in file_list:
            file_url = API_URL + 'pull-framework/' + file_name
            response = requests.get(
                file_url,
                headers={'Authorization': auth_token} if auth_token else None
            )
            if response.status_code == 200:
                file_path = os.path.join(FRAMEWORKS_DIR, file_name)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                with open(file_path, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded {file_name} to {FRAMEWORKS_DIR}")
            else:
                print(f"Error downloading {file_name}: {response.status_code} {response.text}")
    else:
        print(f"Error getting framework directory {dir_name}: {response.status_code} {response.text}")


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: python mod.py <push|pull> <file_path|dir_name> [-password <password> | -auth <auth_token>]")
        sys.exit(1)

    command = sys.argv[1]
    path = sys.argv[2]

    if command == 'push':
        password = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == '-password' else ''
        if os.path.isdir(path):
            push_framework(path, password)
        else:
            push_file(path, password)
    elif command == 'pull':
        auth_token = sys.argv[4] if len(sys.argv) > 4 and sys.argv[3] == '-auth' else ''
        if '/' in path or '\\' in path:
            pull_framework(path, auth_token)
        else:
            pull_file(path, auth_token)
    else:
        print("Unknown command. Use 'push' or 'pull'.")
        sys.exit(1)
