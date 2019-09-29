# pull official base image
FROM nikolaik/python-nodejs

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements
RUN pip install --upgrade pip

# Installing build dependencies
RUN apt-get update && apt-get install -y libpq-dev python-dev netcat

# Installing Gunicorn
RUN pip install gunicorn

# copy project
COPY . /usr/src/app/

RUN chmod +x entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
