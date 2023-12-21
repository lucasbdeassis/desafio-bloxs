FROM python:3.11-slim-buster

WORKDIR /app

ADD . /app

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "bloxs/main.py"]