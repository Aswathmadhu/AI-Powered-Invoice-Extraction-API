import os

from app.services.document_service import load_document
from app.services.ai_service import extract_invoice


async def process_invoice(
    file_path: str,
    content_type: str
):

    images = load_document(
        file_path,
        content_type
    )

    result = extract_invoice(images)

    return result