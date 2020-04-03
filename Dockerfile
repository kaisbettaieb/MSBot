# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.8.1

LABEL maintainer="KAIS BETTAIEB kaisbettaieb@gmail.com"

#RUN apt-get update -y && \
#   apt-get install -y python-pip python-dev
# We copy just the requirements.txt first to leverage Docker cache
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]