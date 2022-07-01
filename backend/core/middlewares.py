import logging
import time

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp

from backend.core.utils.logger import JSONFormatter


# from app.core.utils.logger import APIFilter


class ProcessTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request.state.time_started = time.time()
        response = await call_next(request)
        process_time = time.time() - request.state.time_started
        response.headers["X-Process-Time"] = str(process_time)

        return response


class ActivityLoggerMiddleWare(BaseHTTPMiddleware):

    def __init__(self, app: ASGIApp):
        super().__init__(app)
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)

        self.add_file_handler()
        # self.logger.addFilter(APIFilter())

    def add_file_handler(self):
        file_handler = logging.FileHandler('activity.log')
        file_handler.setFormatter(JSONFormatter())
        self.logger.addHandler(file_handler)

    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        self.logger.info(None, extra={'request': request, 'response': response})

        return response
