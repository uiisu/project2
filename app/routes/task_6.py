from fastapi import APIRouter, HTTPException

from app.core import DataGenerator, JSONWriter, CSVWriter, YAMLWriter
from app.models import SmallJson
from uuid import uuid4

router = APIRouter(tags=["API для хранения файлов"])

"""
Задание_6. 

Изучите следущие классы в модуле app.core: BaseWriter, DataGenerator

API должно принимать json, по типу:
{
    "file_type": "json",  # или "csv", "yaml"
    "matrix_size": int    # число от 4 до 15
}
В ответ на удачную генерацию файла должен приходить id для скачивания.

Добавьте реализацию методов класса DataGenerator.
Добавьте аннотации типов и (если требуется) модели в модуль app.models.

(Подумать, как переисползовать код из задания 5)
"""


@router.post("/generate_file", description="Задание_6. Конвертер")
async def generate_file(body: SmallJson) -> str:
    """
    Принимает json, по типу:
    {
        "file_type": "json",  # или "csv", "yaml"
        "matrix_size": int    # число от 4 до 15
    }
    Генерирует файл.
    Возвращает id для скачивания.
    """

    data = DataGenerator()
    data.generate(body.matrix_size)
    data.file_id = int(uuid4())
    path = f"D:\\Temp\\IBS\\uploaded_files/{data.file_id}.{body.file_type}"
    if body.file_type == "json":
        writer = JSONWriter()
        try:
            data.to_file(path, writer)
        except Exception:
            raise HTTPException(status_code=400, detail="Размер матрицы должен быть от 4 до 15.")
    elif body.file_type == "csv":
        writer = CSVWriter()
        try:
            data.to_file(path, writer)
        except Exception:
            raise HTTPException(status_code=400, detail="Размер матрицы должен быть от 4 до 15.")
    elif body.file_type == "yaml":
        writer = YAMLWriter()
        try:
            data.to_file(path, writer)
        except Exception:
            raise HTTPException(status_code=400, detail="Размер матрицы должен быть от 4 до 15.")
    else:
        raise HTTPException(status_code=400, detail="Тип файла не поддерживается.")
    file_id: int = data.file_id

    return str(file_id)
