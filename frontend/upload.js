function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const message = document.getElementById("message");

    if (fileInput.files.length === 0) {
        message.innerText = "Please select a file to upload.";
        return;
    }

    const file = fileInput.files[0];

    // Allowed file types
    const allowedExtensions = ["png", "jpg", "jpeg", "gif", "mp3", "wav", "ogg", "flac", "mp4", "avi", "mov", "mkv"];

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
            message.innerText = "File uploaded successfully!";
            loadFiles(getCurrentType()); // Refresh uploaded files
        }
    })
    .catch(error => {
        message.innerText = "Error uploading file.";
    });
}

function loadFiles(fileType) {
    fetch(`/list/${fileType}`)
    .then(response => response.json())
    .then(files => {
        const listElement = document.getElementById(fileType + "List");
        listElement.innerHTML = "";
        
        files.forEach(fileUrl => {
            let fileElement;
            if (fileType === "images") {
                fileElement = `<img src="${fileUrl}" alt="Image" width="200">`;
            } else if (fileType === "videos") {
                fileElement = `<video controls width="300"><source src="${fileUrl}" type="video/mp4"></video>`;
            } else if (fileType === "audios") {
                fileElement = `<audio controls><source src="${fileUrl}" type="audio/mp3"></audio>`;
            }
            listElement.innerHTML += `<div>${fileElement}</div>`;
        });
    })
    .catch(error => console.error("Error fetching files:", error));
}

function getCurrentType() {
    if (window.location.pathname.includes("image")) return "images";
    if (window.location.pathname.includes("video")) return "videos";
    if (window.location.pathname.includes("audio")) return "audios";
    return "";
}
