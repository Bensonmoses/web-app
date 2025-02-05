from flask import Flask, render_template, request, jsonify
from azure.storage.blob import BlobServiceClient
import os
import uuid  # For generating unique filenames

app = Flask(__name__, static_folder="../static", template_folder="../templates")

# Azure Storage Configuration
AZURE_STORAGE_CONNECTION_STRING = "BlobEndpoint=https://aiclonefiles.blob.core.windows.net/;QueueEndpoint=https://aiclonefiles.queue.core.windows.net/;FileEndpoint=https://aiclonefiles.file.core.windows.net/;TableEndpoint=https://aiclonefiles.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2025-04-30T06:31:25Z&st=2025-02-04T23:31:25Z&spr=https&sig=bijj7Y7aUOnD9pYfg4KMTeNk5hDJRPm4YZg1UaPsqHw%3D"
STORAGE_ACCOUNT_NAME = "aiclonefiles"

# Azure Containers
CONTAINERS = {
    "images": "ai-clone-images",
    "videos": "ai-clone-videos",
    "audios": "ai-clone-audios",
}

# Initialize Azure Blob Service Client
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    # Determine the correct container based on file type
    file_ext = file.filename.split(".")[-1].lower()

    if file_ext in ["png", "jpg", "jpeg"]:
        container_name = CONTAINERS["images"]
    elif file_ext in ["mp4", "mov", "avi"]:
        container_name = CONTAINERS["videos"]
    elif file_ext in ["mp3", "wav", "ogg"]:
        container_name = CONTAINERS["audios"]
    else:
        return jsonify({"message": "Unsupported file type"}), 400

    # Generate unique filename to prevent overwriting
    unique_filename = f"{uuid.uuid4().hex}_{file.filename}"

    try:
        # Upload to Azure Blob Storage with unique filename
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=unique_filename)
        blob_client.upload_blob(file, overwrite=True)  # Allow overwriting

        file_url = f"https://{STORAGE_ACCOUNT_NAME}.blob.core.windows.net/{container_name}/{unique_filename}"

        return jsonify({"message": "File uploaded successfully!", "file_url": file_url})
    
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
