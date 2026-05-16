FROM python:3.10-slim-buster
WORKER /app
COPY . /app

RUN  apt -y && apt install awscli -y
RUN apt-get update && pip install -r requirements.txt
CMD ["python3","app.py"]