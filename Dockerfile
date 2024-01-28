FROM python:3.6

ENV DockerHOME=/home/app/webapp

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./WebApp $DockerHOME

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000