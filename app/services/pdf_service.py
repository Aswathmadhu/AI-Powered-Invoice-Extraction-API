import pymupdf
from PIL import Image
import io


def pdf_to_images(pdf_path: str):
    document = pymupdf.open(
        pdf_path
    )
    images = []
    for page in document:
        pix = page.get_pixmap(
            matrix=pymupdf.Matrix(2, 2),
            alpha=False
        )
        image_bytes = pix.tobytes("png")
        image = Image.open(
            io.BytesIO(image_bytes)
        ).convert("RGB")
        images.append(image)
    document.close()
    return images