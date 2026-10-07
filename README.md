# AI-Powered-Invoice-Extraction-API

An AI-powered REST API for extracting structured information from invoices in **PDF and image formats** using **Google Gemini Vision**.

The system is designed to handle invoices with different layouts, field positions, terminology, and table structures without requiring template-specific configurations. Extracted information is semantically mapped to a predefined schema and validated using Pydantic before being returned as a consistent JSON response.

Project Overview

Invoice documents often contain the same information but present it in different ways.

A traditional template-based extraction system would require separate rules for each invoice format.

This project uses a vision-capable LLM to understand the invoice semantically and map the extracted information into a predefined response structure.

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

| Technology | Purpose |

| Python 3.11   | Application development |
| FastAPI       | REST API framework |
| Google Gemini | AI-powered invoice understanding |
| PyMuPDF       | PDF rendering and page conversion |
| Pillow        | Image processing |
| Pydantic      | Data modelling and validation |

