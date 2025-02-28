from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
import traceback

class CustomAppException(Exception):
    """
    A custom base exception for our application.
    You can add more specialized exceptions derived from this.
    """
    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)

async def custom_app_exception_handler(request: Request, exc: CustomAppException):
    """
    Custom handler for our CustomAppException.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )


async def generic_exception_handler(request: Request, exc: Exception):
    """
    Catch-all exception handler (for debugging or logging).
    """
    # We can log the traceback here
    return JSONResponse(
        status_code=HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "Internal Server Error",
            "trace": traceback.format_exc()  # or hide in production
        },
    )
