from flask import Flask, request, redirect, render_template
from google.cloud import storage
import config
import os

app = Flask(__name__)

# Initialize GCP storage client
client = storage.Client(project="fair-smoke-440311-i0")
bucket = client.get_bucket(config.BUCKET_NAME)

def allowed_file(filename):
    """Check if the file is allowed based on its extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in config.ALLOWED_EXTENSIONS

def upload_file_to_gcs(file, folder_name):
    """Upload the file to the specified folder in GCS, replacing if file already exists."""
    blob = bucket.blob(f"{folder_name}/{file.filename}")

    # Check if file already exists and delete it if so
    if blob.exists():
        print(f"File {file.filename} already exists. Replacing with the new file.")
        blob.delete()  # Delete the existing file before uploading the new one

    # Upload the new file
    blob.upload_from_string(
        file.read(),
        content_type=file.content_type
    )
    return blob.public_url

@app.route("/", methods=["GET", "POST"])
def upload_file():
    """Handle the file upload request."""
    if request.method == "POST":
        file = request.files["file"]
        folder = request.form["folder"]

        if file and allowed_file(file.filename):
            # Upload to GCS and handle replacement
            file_url = upload_file_to_gcs(file, folder)
            return render_template("index.html", file_url=file_url)  # Optionally, display the uploaded file URL

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)




# gcloud auth application-default login 
