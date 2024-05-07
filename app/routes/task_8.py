from fastapi import APIRouter, Response

router = APIRouter(tags=["Стажировка"])

"""
Задание_8. Декоратор - счётчик запросов.

Напишите декоратор который будет считать кол-во запросов сделанных к приложению.
Оберните роут new_request() этим декоратором.
Подумать, как хранить переменную с кол-вом сделаных запросов.
"""

request_count = 0


def count_requests(func):
    async def wrapper():
        global request_count
        request_count += 1
        return await func()
    return wrapper


@router.get("/new_request", description="Задание_8. Декоратор - счётчик запросов.")
@count_requests
async def new_request():
    """Возвращает кол-во сделанных запросов."""

    return Response(content=f"Кол-во сделанных запросов: {request_count}", media_type="text/plain")
