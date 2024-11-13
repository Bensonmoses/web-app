// File type selection
let selectedType = "";

function selectFileType(type) {
  selectedType = type;
  const fileInput = document.getElementById("fileInput");
  fileInput.accept = selectedType === "images" ? "image/*" : selectedType === "videos" ? "video/*" : selectedType === "audios" ? "audio/*" : "*/*";
  document.getElementById("fileNameDisplay").textContent = `${type.charAt(0).toUpperCase() + type.slice(1)} Files Only`;
  document.getElementById("filePreview").style.display = "none"; // Reset preview
}

// Display selected file name and preview
function showFileName() {
  const fileInput = document.getElementById("fileInput");
  const fileNameDisplay = document.getElementById("fileNameDisplay");
  fileNameDisplay.textContent = fileInput.files[0].name;

  // Show file preview if it's an image
  const filePreview = document.getElementById("filePreview");
  const file = fileInput.files[0];
  if (file && file.type.startsWith("image/")) {
    const reader = new FileReader();
    reader.onload = function (e) {
      filePreview.src = e.target.result;
      filePreview.style.display = "block";
    };
    reader.readAsDataURL(file);
  } else {
    filePreview.style.display = "none";
  }
}

// Handle upload progress and submit form
document.getElementById("uploadForm").addEventListener("submit", function (e) {
  e.preventDefault(); // Prevent the default form submission
  const formData = new FormData(this);
  
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/upload", true); // Change '/upload' if needed

  // Update progress bar
  xhr.upload.onprogress = function (event) {
    const progressBar = document.getElementById("progressBar");
    const progress = document.getElementById("progress");
    progressBar.style.display = "block";
    if (event.lengthComputable) {
      const percentComplete = (event.loaded / event.total) * 100;
      progress.style.width = percentComplete + "%";
    }
  };

  // On upload complete
  xhr.onload = function () {
    if (xhr.status === 200) {
      alert("File uploaded successfully!");
      document.getElementById("progressBar").style.display = "none";
      document.getElementById("fileNameDisplay").textContent = "No file chosen";
      document.getElementById("fileInput").value = "";
      document.getElementById("filePreview").style.display = "none";
    } else {
      alert("Upload failed. Please try again.");
    }
  };

  // Send the form data
  xhr.send(formData);
});
