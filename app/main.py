from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.api.api import api_router

app = FastAPI(
    title="Receipt Processor",
    description="A simple receipt processor",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(api_router)

# note - this is just an override for the default request validation response, instead of returning 422, we want to return 400, per the api.yml spec
# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return JSONResponse(
#         status_code=status.HTTP_400_BAD_REQUEST,
#         content={"detail": exc.errors()},
#     )
