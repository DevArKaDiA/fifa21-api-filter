# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Get the Real World example app
RUN git clone https://github.com/DevArKaDiA/fifa21-api-filter.git /src

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /src/FifaService/

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# VOLUME /code

EXPOSE 8000
CMD python manage.py makemigrations && python manage.py migrate && python manage.py seedFromApi && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]