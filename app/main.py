from fastapi import FastAPI
from app.api.api import api_router

app = FastAPI(
    title="receipt-processor-challenge",
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(api_router)
