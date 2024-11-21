from flask import Flask, request, jsonify, send_file, render_template
import os
from werkzeug.utils import secure_filename
from doc_processor import extract_metadata, convert_docx_to_pdf

app = Flask(__name__, template_folder=r"C:\Users\yashp\OneDrive\Desktop\doc-to-pdf-converter\templates",
                      static_folder=r"C:\Users\yashp\OneDrive\Desktop\doc-to-pdf-converter\static")

# Configuration
UPLOAD_FOLDER = "uploads"
PDF_FOLDER = PDF_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../pdfs"))
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PDF_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["PDF_FOLDER"] = PDF_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {"docx"}


def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Serve the main HTML page
@app.route("/")
def index():
    """
    Serve the main HTML page.
    """
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    """
    Endpoint to upload a .docx file.
    Returns the file metadata after successful upload.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        try:
            metadata = extract_metadata(file_path)
            return jsonify({"message": "File uploaded successfully", "metadata": metadata}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid file type. Only .docx files are allowed."}), 400


@app.route("/convert", methods=["POST"])
def convert_file():
    """
    Endpoint to convert a .docx file to a PDF.
    Accepts optional password protection for the PDF.
    """
    data = request.json
    if not data or "filename" not in data:
        return jsonify({"error": "Filename is required"}), 400

    filename = secure_filename(data["filename"])
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404

    password = data.get("password")  # Optional password
    pdf_output_path = os.path.join(app.config["PDF_FOLDER"], filename.replace(".docx", ".pdf"))

    try:
        convert_docx_to_pdf(file_path, pdf_output_path, password)
        return jsonify({"message": "File converted successfully", "pdf_path": pdf_output_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/download", methods=["GET"])
def download_file():
    """
    Endpoint to download the converted PDF file.
    """
    pdf_filename = request.args.get("filename")  # Get the filename from the request

    if not pdf_filename:
        return jsonify({"error": "Filename is required"}), 400

    pdf_path = os.path.join(app.config["PDF_FOLDER"], secure_filename(pdf_filename))

    # Check if the file exists
    if not os.path.exists(pdf_path):
        return jsonify({"error": f"File not found: {pdf_filename}"}), 404

    return send_file(pdf_path, as_attachment=True, download_name=pdf_filename)


@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors.
    """
    return jsonify({"error": "An internal server error occurred"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
