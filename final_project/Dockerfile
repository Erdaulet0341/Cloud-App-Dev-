FROM python:3.9
WORKDIR /code
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY .. .
RUN chmod +x ./start.sh
CMD ["./start.sh"]

#  1 docker build -t django-app .
#  2 docker run -p 8000:8000 django-app
#    python manage.py djangoviz