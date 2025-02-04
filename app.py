from flask import Flask, request, render_template
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

# Azure Blob Storage Connection String (Replace with your actual connection string)
AZURE_STORAGE_CONNECTION_STRING = "BlobEndpoint=https://aiclonefiles.blob.core.windows.net/;QueueEndpoint=https://aiclonefiles.queue.core.windows.net/;FileEndpoint=https://aiclonefiles.file.core.windows.net/;TableEndpoint=https://aiclonefiles.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2025-05-01T02:08:30Z&st=2025-02-04T19:08:30Z&spr=https&sig=OvBpGJIa1fe3DdAwK9Gk7oa4pPk5i%2B2wrfjx%2F7Mbx6s%3D"
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

# Allowed containers in Azure Blob Storage
ALLOWED_CONTAINERS = ["ai-clone-images", "ai-clone-videos", "ai-clone-audios"]

@app.route("/", methods=["GET", "POST"])
def upload_file():
    message = ""

    if request.method == "POST":
        file = request.files.get("file")
        container_name = request.form.get("container")

        if file and container_name in ALLOWED_CONTAINERS:
            blob_client = blob_service_client.get_blob_client(container=container_name, blob=file.filename)
            blob_client.upload_blob(file, overwrite=True)
            message = f"✅ File '{file.filename}' uploaded to '{container_name}' successfully!"

    return render_template("index.html", message=message, allowed_containers=ALLOWED_CONTAINERS)

if __name__ == "__main__":
    app.run(debug=True)
