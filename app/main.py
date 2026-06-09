from fastapi import FastAPI, HTTPException, UploadFile, File
import os
import shutil

app = FastAPI(
    title="AxiomCheck API",
    description="Backend API for checking technical integrity of research papers.",
    version="0.1.0"
)

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def root():
    return {
        "message": "Welcome to AxiomCheck API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "AxiomCheck API"
    }


@app.post("/upload")
def upload_manuscript(file: UploadFile = File(...)):
    filename = file.filename

    if filename is None:
        raise HTTPException(
        status_code=400,
        detail="No file name found."
    )

    if not filename.lower().endswith(".pdf"):
        raise HTTPException(
        status_code=400,
        detail="Only PDF files are allowed for now."
    )

    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file_size = os.path.getsize(file_path)

    return {
        "success": True,
        "message": "File uploaded successfully.",
        "filename": filename,
        "file_path": file_path,
        "file_size_bytes": file_size
    }