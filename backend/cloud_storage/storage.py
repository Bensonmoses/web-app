from azure.storage.blob import BlobServiceClient
from backend.config import AZURE_STORAGE_CONNECTION_STRING, AUDIO_CONTAINER, VIDEO_CONTAINER, IMAGE_CONTAINER
import uuid  # For generating unique filenames

# Initialize Azure Blob Service Client
blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)

def upload_to_azure(file, filename):
    """Uploads a file to the correct Azure Blob Storage container based on file type."""
    # Determine correct container based on file type
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif")):
        container_name = IMAGE_CONTAINER
    elif filename.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):
        container_name = VIDEO_CONTAINER
    elif filename.lower().endswith((".mp3", ".wav", ".ogg", ".flac")):
        container_name = AUDIO_CONTAINER
    else:
        return None, "Unsupported file type"

    try:
        container_client = blob_service_client.get_container_client(container_name)

        # Generate a unique filename to prevent overwriting
        unique_filename = f"{uuid.uuid4().hex}_{filename}"

        blob_client = container_client.get_blob_client(unique_filename)

        # Upload the file (allow overwrite)
        blob_client.upload_blob(file, overwrite=True)

        file_url = f"https://{blob_client.account_name}.blob.core.windows.net/{container_name}/{unique_filename}"
        return file_url, None

    except Exception as e:
        return None, f"Azure Upload Error: {str(e)}"

def list_files_from_container(container_name):
    """Lists all files in a specific Azure Blob Storage container."""
    try:
        container_client = blob_service_client.get_container_client(container_name)
        return [blob.name for blob in container_client.list_blobs()]
    except Exception as e:
        return f"Error retrieving files: {str(e)}"
