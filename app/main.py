import os
import uuid

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    HTTPException
)

from app.services.invoice_service import process_invoice

app = FastAPI(
    title="AI Invoice Extraction API",
    description="AI-powered invoice extraction and field mapping API",
    # version="1.0.0"
)

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

ALLOWED_TYPES = {
    "application/pdf",
    "image/jpeg",
    "image/png",
    "image/webp"
}
@app.get("/")
def root():

    return {
        "message": "AI Invoice Extraction API",
        "status": "running"
    }


@app.post("/api/v1/invoice/extract")
async def extract_invoice(
    file: UploadFile = File(...)
):

    if file.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported file type. "
                "Upload PDF, JPG, JPEG, PNG or WEBP."
            )
        )

    extension = os.path.splitext(file.filename)[1]

    filename = (
        f"{uuid.uuid4()}"
        f"{extension}"
    )

    file_path = os.path.join(
        UPLOAD_DIR,
        filename
    )

    try:
        contents = await file.read()
        with open(
            file_path,
            "wb"
        ) as f:
            f.write(contents)
        result = await process_invoice(
            file_path=file_path,
            content_type=file.content_type
        )
        return result.model_dump()

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)