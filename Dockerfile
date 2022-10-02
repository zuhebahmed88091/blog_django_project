# pull the official base image
FROM python:3.9.10-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt
# copy project
COPY . /usr/src/app

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
