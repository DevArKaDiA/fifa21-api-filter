FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /FifaService
WORKDIR /FifaService
ADD requirements.txt /FifaService/
RUN pip install -r requirements.txt
ADD . /FifaService/
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000