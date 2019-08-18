FROM python:3
WORKDIR /app

RUN pip install flask mysql-connector-python

COPY *.py ./
COPY static ./static/
COPY templates ./templates/

CMD ["python", "./server.py"]
