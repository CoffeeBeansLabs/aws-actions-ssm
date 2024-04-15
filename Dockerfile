FROM python:3.12.3-slim

RUN apt-get update
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src/ .
WORKDIR /

ENTRYPOINT ["python", "aws_ssm.py"]