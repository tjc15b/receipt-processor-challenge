from fastapi import APIRouter, HTTPException, status
from app.api.schemas.receipt import ReceiptPayload
import uuid
from app.api.utils import calculate_points

router = APIRouter()

receipt_db = {}

@router.post(
    "/process",
)
async def process(
    receipt: ReceiptPayload
):
    receipt_uuid = str(uuid.uuid4())

    points = await calculate_points(receipt)

    receipt_db[receipt_uuid] = {
        "id": receipt_uuid,
        "points": points,
        **receipt.model_dump()
    }

    return {"id": receipt_uuid}

@router.get(
    "/{id}/points"
)
async def get_points(id: str):
    receipt = receipt_db.get(id)
    if not receipt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Receipt with id {id} not found."
        )
    
    return receipt.get("points")
