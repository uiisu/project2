FROM python:3.10-buster

WORKDIR /education1

COPY ./requirements.txt /education1/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /education1/requirements.txt

COPY ./app /education1/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]