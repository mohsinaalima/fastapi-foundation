from fastapi.responces import JSONResponse
from fastapi.requests import Request

class PinCodeNotFoundError(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode

class InvalidPinCodeError(Exception):
    def _init__(self, pincode: str, reason: str="Invalid pincode format"):
        self.pincode = pincode 
        self.reason = reason

async def pincode_not_found_exception_handler(request: Request, exc: PinCodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": f"Pincode {exc.pincode} not found."},
    )        


