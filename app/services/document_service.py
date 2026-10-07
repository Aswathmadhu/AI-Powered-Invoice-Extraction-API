from PIL import Image
from .pdf_service import pdf_to_images


SUPPORTED_IMAGE_TYPES = {
    "image/jpeg",
    "image/png",
    "image/webp"
}


def load_document(file_path: str, content_type: str):

    if content_type == "application/pdf":
        return pdf_to_images(file_path)

    if content_type in SUPPORTED_IMAGE_TYPES:
        image = Image.open(file_path).convert("RGB")
        return [image]

    raise ValueError(
        "Unsupported file type. "
        "Upload PDF, JPG, JPEG, PNG or WEBP."
    )