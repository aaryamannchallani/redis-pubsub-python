FROM python:latest

WORKDIR /app

COPY ./lib/ .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "publisher.py"]
