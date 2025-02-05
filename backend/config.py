import os

# Azure Blob Storage Configuration
AZURE_STORAGE_CONNECTION_STRING = "BlobEndpoint=https://aiclonefiles.blob.core.windows.net/;QueueEndpoint=https://aiclonefiles.queue.core.windows.net/;FileEndpoint=https://aiclonefiles.file.core.windows.net/;TableEndpoint=https://aiclonefiles.table.core.windows.net/;SharedAccessSignature=sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2025-04-30T06:31:25Z&st=2025-02-04T23:31:25Z&spr=https&sig=bijj7Y7aUOnD9pYfg4KMTeNk5hDJRPm4YZg1UaPsqHw%3D"

# Containers for different media types
AUDIO_CONTAINER = "ai-clone-audios"
VIDEO_CONTAINER = "ai-clone-videos"
IMAGE_CONTAINER = "ai-clone-images"
