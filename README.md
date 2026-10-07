# AI-Powered-Invoice-Extraction-API

An AI-powered REST API for extracting structured information from invoices in **PDF and image formats** using **Google Gemini Vision**.

The system is designed to handle invoices with different layouts, field positions, terminology, and table structures without requiring template-specific configurations. Extracted information is semantically mapped to a predefined schema and validated using Pydantic before being returned as a consistent JSON response.

Project Overview

Invoice documents often contain the same information but present it in different ways.

A traditional template-based extraction system would require separate rules for each invoice format.

This project uses a vision-capable LLM to understand the invoice semantically and map the extracted information into a predefined response structure.

Core workflow:-

              Invoice PDF / Image
                        │
                        ▼
                 FastAPI Upload
                        │
                        ▼
               Document Processing
                        │
              ┌─────────┴─────────┐
              │                   │
            PDF                 Image
              │                   │
              ▼                   │
          PyMuPDF                 │
        PDF → Images              │
              │                   │
              └─────────┬─────────┘
                        ▼
                 Gemini Vision
                        │
                        ▼
              Invoice Understanding
                        │
                        ▼
              Semantic Field Mapping
                        │
                        ▼
                Pydantic Validation
                        │
                        ▼
          Business Validation / Calculation
                        │
                        ▼
              Structured JSON Response

              
Features

- PDF invoice processing
- JPG/JPEG image invoice processing
- PNG image invoice processing
- WEBP image invoice processing
- Multi-page PDF support
- AI-powered invoice understanding
- Vision-based text and data extraction
- Semantic field mapping
- Layout-independent extraction
- Line-item extraction
- Customer information extraction
- Tax/VAT extraction
- Pydantic schema validation
- Deterministic financial calculations
- REST API using FastAPI
- Automatic Swagger/OpenAPI documentation
- Temporary uploaded-file handling

Technology Stack

| Python 3.11
| FastAPI  
| Google Gemini 
| PyMuPDF  
| Pillow
| Pydantic   


Installation
------------
1. Clone the repository
2. Create a virtual environment
python3 -m venv venv

Activate it:
macOS/Linux :source venv/bin/activate
Windows :venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

Configuration
-------------
Create a .env file in the project root:
GEMINI_API_KEY=your_gemini_api_key

A .env.example file should contain only:

GEMINI_API_KEY=your_gemini_api_key

Running the Application
-----------------------
Start the FastAPI server:
uvicorn app.main:app --reload
 
The API will be available at:
http://127.0.0.1:8000/docs
