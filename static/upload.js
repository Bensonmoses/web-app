function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const message = document.getElementById("message");

    if (fileInput.files.length === 0) {
        message.innerText = "Please select a file to upload.";
        return;
    }

    const file = fileInput.files[0];

    // Allowed file types
    const allowedExtensions = ["png", "jpg", "jpeg", "mp3", "wav", "ogg", "mp4", "mov", "avi"];

    const fileExt = file.name.split(".").pop().toLowerCase();
    if (!allowedExtensions.includes(fileExt)) {
        message.innerText = "Invalid file type! Only images, audio, and video files are allowed.";
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    fetch("/upload", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.message.includes("Error")) {
            message.innerText = "Error: " + data.message;
        } else {
            message.innerText = "File uploaded successfully! URL: " + data.file_url;
            console.log("File URL:", data.file_url);
        }
    })
    .catch(error => {
        message.innerText = "Error uploading file.";
    });
}
