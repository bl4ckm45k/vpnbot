# noinspection
import logging
import os
import ssl

import uvicorn
from cryptography import x509
from cryptography.hazmat.backends import default_backend

from app import app, logger
from config import (DEBUG, UVICORN_HOST, UVICORN_PORT, UVICORN_SSL_CERTFILE,
                    UVICORN_SSL_KEYFILE, UVICORN_UDS)

if __name__ == "__main__":
    try:
        uvicorn.run(
            "main:app",
            host=('0.0.0.0' if DEBUG else UVICORN_HOST),
            port=UVICORN_PORT,
            uds=(None if DEBUG else UVICORN_UDS),
            ssl_certfile=UVICORN_SSL_CERTFILE,
            ssl_keyfile=UVICORN_SSL_KEYFILE,
            workers=1,
            reload=DEBUG,
            log_level=logging.DEBUG if DEBUG else logging.INFO
        )
    except FileNotFoundError:  # to prevent error on removing unix sock
        pass
