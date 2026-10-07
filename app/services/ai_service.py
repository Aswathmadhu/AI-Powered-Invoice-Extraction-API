import os
import json
import io

from dotenv import load_dotenv
from PIL import Image
from google import genai
from google.genai import types

from app.models.invoice import InvoiceResponse
from app.prompts.invoice_prompt import INVOICE_EXTRACTION_PROMPT


# Load environment variables
load_dotenv()


# Get Gemini API key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. "
        "Please add it to your .env file."
    )


# Create Gemini client
client = genai.Client(
    api_key=api_key
)


def image_to_bytes(image: Image.Image) -> bytes:
    """
    Convert PIL image to JPEG bytes.
    """

    buffer = io.BytesIO()

    image.save(
        buffer,
        format="JPEG",
        quality=90
    )

    return buffer.getvalue()


def extract_invoice(images):
    """
    Send invoice images to Gemini
    and extract structured invoice data.
    """

    contents = [
        INVOICE_EXTRACTION_PROMPT
    ]

    # Add invoice pages
    for image in images:

        image_bytes = image_to_bytes(image)

        contents.append(
            types.Part.from_bytes(
                data=image_bytes,
                mime_type="image/jpeg"
            )
        )


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=InvoiceResponse,
            temperature=0
        )
    )


    # Parse Gemini response
    result = json.loads(
        response.text
    )


    # Validate using Pydantic
    invoice = InvoiceResponse(
        **result
    )


    return invoice