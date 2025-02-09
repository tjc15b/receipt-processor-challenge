from pydantic import BaseModel

class ItemPayload(BaseModel):
    shortDescription: str
    price: str

class ReceiptPayload(BaseModel):
    retailer: str
    purchaseDate: str
    purchaseTime: str
    items: list[ItemPayload]
    total: str
