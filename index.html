from flask import Flask, request, redirect, render_template
from azure.storage.blob import BlobServiceClient
import os

app = Flask(__name__)

# Azure Blob Storage Connection String (Replace with your actual connection string)
AZURE_STORAGE_CONNECTION_STRING = "YOUR_AZURE_STORAGE_CONNECTION_STRING"
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

# Allowed containers in Azure Blob Storage
ALLOWED_CONTAINERS = ["ai-clone-images", "ai-clone-videos", "ai-clone-audios"]

# Allowed file extensions
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "mp4", "mp3", "wav", "avi"}

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file_to_azure(file, container_name):
    """Upload the file to Azure Blob Storage, replacing it if it already exists."""
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.filename)

    # Delete existing file before uploading new one
    try:
        blob_client.delete_blob()
        print(f"Existing file '{file.filename}' deleted.")
    except Exception as e:
        print(f"No existing file found: {e}")

    # Upload new file
    blob_client.upload_blob(file, overwrite=True)
    return f"File '{file.filename}' uploaded to {container_name} container successfully!"

@app.route("/", methods=["GET", "POST"])
def upload_file():
    """Handle file upload request."""
    if request.method == "POST":
        file = request.files["file"]
        container_name = request.form["container"]

        if file and allowed_file(file.filename) and container_name in ALLOWED_CONTAINERS:
            message = upload_file_to_azure(file, container_name)
            return render_template("index.html", message=message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
