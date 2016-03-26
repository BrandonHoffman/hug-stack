FROM python:alpine

ENV app=app

RUN pip install hug
RUN pip install gunicorn
RUN echo $app

ADD $app app

EXPOSE 8000

CMD hug -f /app/__init__.py -p 8000
