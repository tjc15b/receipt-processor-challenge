from datetime import time
import math
from app.api.schemas.receipt import Receipt

async def calculate_points(receipt: Receipt):
    points_total = 0

    # One point for every alphanumeric character in the retailer name.
    points_total += sum(char.isalnum() for char in receipt.retailer)

    # 50 points if the total is a round dollar amount with no cents.
    total = float(receipt.total)
    if total.is_integer():
        points_total += 50

    # 25 points if the total is a multiple of 0.25.
    if (total * 100) % 25 == 0:
        points_total += 25

    # 5 points for every two items on the receipt.
    points_total += (len(receipt.items) // 2) * 5

    # If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    for item in receipt.items:
        description = item.shortDescription.strip()
        price = float(item.price)
        if len(description) % 3 == 0:
            points_total += math.ceil(price * 0.2)

    # 6 points if the day in the purchase date is odd.
    if receipt.purchaseDate:
        day = receipt.purchaseDate.day
        if day % 2 != 0:
            points_total += 6

    # 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    if receipt.purchaseTime:
        purchase_time_obj = receipt.purchaseTime
        if time(14, 0) <= purchase_time_obj <= time(15, 59):
            points_total += 10

    return points_total
