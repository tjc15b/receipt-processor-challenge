from pydantic import BaseModel, Field
from typing import List
from datetime import date, time

class Item(BaseModel):
    shortDescription: str = Field(..., description="The Short Product Description for the item.", pattern=r"^[\w\s\-]+$", example="Mountain Dew 12PK")
    price: str = Field(..., pattern=r"^\d+\.\d{2}$", description="The total price payed for this item.", example="6.49")

class Receipt(BaseModel):
    retailer: str = Field(..., pattern=r"^[\w\s\-\&]+$", description="The name of the retailer or store the receipt is from.", example="M&M Corner Market")
    purchaseDate: date = Field(..., description="The date of the purchase printed on the receipt.", example="2022-01-01")
    purchaseTime: time = Field(..., description="The time of the purchase printed on the receipt. 24-hour time expected.", example="13:01")
    items: List[Item] = Field(..., min_length=1)
    total: str = Field(..., pattern=r"^\d+\.\d{2}$", description="The total amount paid on the receipt.", example="6.49")

class ProcessResponse(BaseModel):
    id: str = Field(..., pattern=r"^\S+$", example="adb6b560-0eef-42bc-9d16-df48f30e89b2")

class PointsResponse(BaseModel):
    points: int = Field(..., example=100)
