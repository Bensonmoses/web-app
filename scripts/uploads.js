function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const message = document.getElementById("message");

    if (fileInput.files.length === 0) {
        message.innerText = "Please select a file to upload.";
        return;
    }

    const file = fileInput.files[0];
    message.innerText = `Uploading ${file.name}...`;

    setTimeout(() => {
        message.innerText = "File uploaded successfully!";
    }, 2000); // Simulate upload delay
}
