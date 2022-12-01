FROM python:3.12.0a2-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
#RUN chmod 777 -R /var/lib/postgresql/data
#RUN chmod 777 -R /tmp
RUN apt update && apt install -y && apt -y install libpq-dev build-essential
COPY requirements.txt /code/ 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 
COPY . /code/
EXPOSE 8000
