from pydantic import BaseModel, Field
from typing import List


class InvoiceHeader(BaseModel):
    invoice_no: str = ""
    invoice_date: str = ""
    due_date: str = ""
    customer: str = ""
    customer_code: str = ""
    address: str = ""
    phno: str = ""
    email: str = ""
    tax_registration_no: str = ""
    currency: str = ""
    payment_terms: str = ""
    narration: str = ""


class InvoiceItem(BaseModel):
    product_name: str = ""
    product_code: str = ""
    description: str = ""
    unit: str = ""

    qty: float = 0
    rate: float = 0
    gross: float = 0
    discount: float = 0
    vat_rate: float = 0
    vat: float = 0
    net: float = 0


class InvoiceResponse(BaseModel):
    header: InvoiceHeader
    body: List[InvoiceItem] = Field(default_factory=list)