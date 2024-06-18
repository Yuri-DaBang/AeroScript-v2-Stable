# start.py
import subprocess
import time

# Start the Flask server
print("Starting Server...")
server_process = subprocess.Popen(['python', 'server/ServerApp.py'])

# Wait for the server to start
print("Waiting for the server to start...")
time.sleep(10)  # Increased sleep time to ensure the server starts

# Check if the server is running
try:
    import requests
    response = requests.get('http://127.0.0.1:5000')
    if response.status_code == 200:
        print("Server is running.")
    else:
        print(f"Server is not running. Status code: {response.status_code}")
except Exception as e:
    print(f"Error checking server status: {e}")
    server_process.terminate()
    exit(1)

# Start the CLI app
#print("Starting Cli...")
#cli_process = subprocess.Popen(['python', 'cli/CliApp.py', 'abc.gg'])

# Wait for the CLI app to finish
#cli_process.wait()

# Optionally, terminate the server after the CLI app finishes
#server_process.terminate()
