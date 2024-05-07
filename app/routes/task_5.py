from fastapi import APIRouter, UploadFile
from fastapi.responses import FileResponse
from uuid import uuid4
import zipfile


router = APIRouter(tags=["API для хранения файлов"])

"""
Задание_5. API для хранения файлов

a.	Написать API для добавления(POST) "/upload_file" и скачивания (GET) "/download_file/{id}" файлов. 
В ответ на удачную загрузку файла должен приходить id для скачивания. 
b.	Добавить архивирование к post запросу, то есть файл должен сжиматься и сохраняться в ZIP формате.
с*.Добавить аннотации типов.
"""
files = {}


@router.post("/upload_file", description="Задание_5. API для хранения файлов")
async def upload_file(file: UploadFile):
    """
    Добавляет файл и архив с файлом в zip формате.
    Возвращает id для скачивания.
    """

    file_id = int(uuid4())
    file_path = f"D:\\Temp\\IBS\\uploaded_files/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(file.file.read())

    zip_file_path = f"D:\\Temp\\IBS\\uploaded_files/{file_id}.zip"
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        zipf.write(file_path, arcname=file.filename)

    files[file_id] = {
        "filename": file.filename,
        "zip_path": zip_file_path
    }
    return str(file_id)


@router.get("/download_file/{file_id}", description="Задание_5. API для хранения файлов")
async def download_file(file_id: int):
    """Скачивает файл."""

    file_info = files.get(file_id)
    filename = file_info["filename"]
    file_path = f"D:\\Temp\\IBS\\uploaded_files/{filename}"
    return FileResponse(file_path)
