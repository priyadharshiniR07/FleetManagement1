FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["sh", "-c", "python manage.py migrate && gunicorn --bind 0.0.0.0:8000 app.wsgi:application"]