FROM python:3.10

WORKDIR app

COPY requirements.txt requirements.txt
COPY django_stripe django_stripe
COPY .env .env

RUN pip install -r requirements.txt

WORKDIR django_stripe

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]