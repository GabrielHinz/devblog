FROM python:3.8

RUN apt-get update && apt-get install -y nginx
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

COPY proxy/default.conf /etc/nginx/sites-available/default

WORKDIR /www

COPY ./app /www

RUN pip install -U pip
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /www/media
RUN chmod -R 755 /www/media

EXPOSE 80

CMD service nginx start && python manage.py runserver 0.0.0.0:8000
