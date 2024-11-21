// Select DOM elements
const uploadForm = document.getElementById("uploadForm");
const docxFileInput = document.getElementById("docxFile");
const metadataSection = document.getElementById("metadata");
const convertForm = document.getElementById("convertForm");
const passwordInput = document.getElementById("password");
const downloadSection = document.getElementById("downloadSection");
const downloadLink = document.getElementById("downloadLink");

// Function to display metadata
function showMetadata(metadata) {
    metadataSection.innerHTML = `
        <h3>File Metadata</h3>
        <p><strong>Title:</strong> ${metadata.title || "N/A"}</p>
        <p><strong>Author:</strong> ${metadata.author || "N/A"}</p>
        <p><strong>Created:</strong> ${metadata.created || "N/A"}</p>
        <p><strong>Last Modified:</strong> ${metadata.last_modified || "N/A"}</p>
        <p><strong>Subject:</strong> ${metadata.subject || "N/A"}</p>
        <p><strong>Keywords:</strong> ${metadata.keywords || "N/A"}</p>
    `;
    metadataSection.style.display = "block";
}

// Upload File
uploadForm.addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent form submission

    const file = docxFileInput.files[0];

    if (!file) {
        alert("Please select a file to upload.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            const error = await response.json();
            alert(`Error: ${error.error}`);
            return;
        }

        const data = await response.json();
        alert("File uploaded successfully!");
        showMetadata(data.metadata);
    } catch (error) {
        alert("An error occurred while uploading the file.");
        console.error(error);
    }
});

// Convert File
convertForm.addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent form submission

    const password = passwordInput.value;
    const file = docxFileInput.files[0];

    if (!file) {
        alert("Please upload a file first.");
        return;
    }

    const filename = file.name;

    try {
        const response = await fetch("/convert", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                filename: filename,
                password: password || null, // Optional password
            }),
        });

        if (!response.ok) {
            const error = await response.json();
            alert(`Error: ${error.error}`);
            return;
        }

        const data = await response.json();
        alert("File converted successfully!");
        downloadLink.href = `/download?filename=${encodeURIComponent(
            filename.replace(".docx", ".pdf")
        )}`;
        downloadSection.style.display = "block";
    } catch (error) {
        alert("An error occurred during the conversion process.");
        console.error(error);
    }
});
