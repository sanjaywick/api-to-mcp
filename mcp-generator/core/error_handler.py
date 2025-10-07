import logging
from fastapi.responses import JSONResponse
from fastapi import Request

# Setup logging
logging.basicConfig(
    filename="mcp_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_error(error: Exception, context: str = ""):
    """
    Logs the error with optional context information
    """
    message = f"{context} - {str(error)}" if context else str(error)
    logging.error(message)

def handle_request_exception(error: Exception):
    """
    Returns a standardized JSON response for request errors
    """
    log_error(error, "Request Exception")
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": f"Request error: {str(error)}"}
    )

def handle_http_error(error: Exception, status_code: int = 500, response_text: str = ""):
    """
    Returns a standardized JSON response for HTTP errors
    """
    log_error(error, f"HTTP Error {status_code}")
    return JSONResponse(
        status_code=status_code,
        content={"status": "error", "message": f"HTTP error: {str(error)}", "response": response_text}
    )

def handle_generic_error(error: Exception, context: str = ""):
    """
    Returns a standardized JSON response for any unexpected error
    """
    log_error(error, context)
    return JSONResponse(
        status_code=500,
        content={"status": "error", "message": f"Unexpected server error: {str(error)}"}
    )
