import logging
from contextvars import ContextVar
from datetime import datetime
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

output_log = logging.getLogger("output")
client_host: ContextVar[str | None] = ContextVar("client_host", default=None)

"""
Задание_7. Логирование в FastAPI с использованием middleware.

Написать конфигурационный файл для логгера "output"
Формат выводимых логов:
[CURRENT_DATETIME] {file: line} LOG_LEVEL - | EXECUTION_TIME_SEC | HTTP_METHOD | URL | STATUS_CODE |
[2023-12-15 00:00:00] {example:62} INFO | 12 | GET | http://localhost/example | 200 |


Дописать класс CustomMiddleware.
Добавить middleware в приложение (app).
"""

logging.basicConfig(
    filename='output.log',
    level=logging.INFO,
    format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - | %(message)s |",
    datefmt="%Y-%m-%d %H:%M:%S",
)


class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        """Load request ID from headers if present. Generate one otherwise."""
        client_host.set(request.client.host)
        output_log.info(f"Accepted request {request.method} {request.url}")
        start_time = datetime.now()
        try:
            response = await call_next(request)
            execution_time_sec = (datetime.now() - start_time).total_seconds()
            output_log.info(
                f"[{datetime.now().isoformat()}] {{{__file__}:{10}}} INFO | {execution_time_sec:.2f} | "
                f"{request.method} | {request.url.path} | {response.status_code} |"
            )
            return response
        except Exception as e:
            output_log.error(f"Internal Server Error: {e}")
            response = Response("Internal Server Error", status_code=500)

            return response
