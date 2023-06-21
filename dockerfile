FROM python:3.9

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . django-project

WORKDIR /django-project

EXPOSE 8000

ENTRYPOINT [ "python3", "manage.py" ]
CMD ["runserver", "0.0.0.0:8000"]