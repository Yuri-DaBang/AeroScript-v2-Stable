# cli/CliApp.py
import os
import requests
import sys

API_URL = 'http://127.0.0.1:5000/get/'
AREOMOD_DIR = os.path.join(os.path.dirname(__file__), 'aeromod')

def download_file(package_name):
    try:
        response = requests.get(API_URL + package_name, stream=True)
        response.raise_for_status()  # Check for HTTP errors

        os.makedirs(AREOMOD_DIR, exist_ok=True)
        file_path = os.path.join(AREOMOD_DIR, package_name)
        
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f'Downloaded {package_name} to {AREOMOD_DIR}')
    except requests.RequestException as e:
        print(f'Error downloading {package_name}: {e}')
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python cli.py <package_name>')
        sys.exit(1)
    
    package_name = sys.argv[1]
    download_file(package_name)
