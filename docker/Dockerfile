FROM python:3.9

MAINTAINER Daniel Dias
COPY . /var/www
WORKDIR /var/www
RUN pip install -r requirements.txt
RUN python app/install.py

EXPOSE 5000
CMD ["python", "app/main.py"]
