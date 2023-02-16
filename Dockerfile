FROM python:3-alpine

WORKDIR /app

RUN apk update
RUN apk upgrade

COPY . .
COPY requirements.txt requirements.txt

RUN python -m pip install --user virtualenv
RUN which python

RUN pip install -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["sh", "-c", "waitress-serve --call 'app:app.create_app'"]