import requests
import hashlib
import os

SERVER_URL = 'http://server:5000/file'
DATA_DIR = '/clientdata'

def download_file():
    response = requests.get(SERVER_URL)
    file_content = response.content
    checksum = response.json().get('checksum')

    file_path = os.path.join(DATA_DIR, 'data.txt')
    with open(file_path, 'wb') as f:
        f.write(file_content)

    # Verify the checksum
    with open(file_path, 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()

    if file_hash == checksum:
        print("File downloaded and checksum verified.")
    else:
        print("Checksum verification failed.")

if __name__ == '__main__':
    download_file()
