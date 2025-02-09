from fastapi import APIRouter, HTTPException, status, Path
from app.api.schemas.receipt import Receipt, PointsResponse, ProcessResponse
from pydantic import ValidationError
import uuid
from app.api.utils import calculate_points

router = APIRouter()

receipt_db = {}

@router.post(
    "/process",
    summary="Submits a receipt for processing.",
    description="Submits a receipt for processing.",
    response_model=ProcessResponse,
)
async def process(
    receipt: Receipt
):
    try:
        receipt_uuid = str(uuid.uuid4())

        points = await calculate_points(receipt)

        receipt_db[receipt_uuid] = {
            "id": receipt_uuid,
            "points": points,
            **receipt.model_dump()
        }

        return {"id": receipt_uuid}
    except ValidationError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The receipt is invalid."
        )

@router.get(
    "/{id}/points",
    summary="Returns the points awarded for the receipt.",
    description="Returns the points awarded for the receipt.",
    response_model=PointsResponse
)
async def get_points(
    id: str = Path(..., description="The ID of the receipt.", pattern=r"^\S+$")
):
    receipt = receipt_db.get(id)
    if not receipt:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No receipt found for that ID."
        )
    
    return {"points": receipt.get("points")}
