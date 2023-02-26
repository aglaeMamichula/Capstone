FROM nginx
COPY . /usr/share/nginx/html
FROM pypy:latest
WORKDIR .
COPY . /
EXPOSE 8000
RUN pip install -r requirements.txt  
CMD python manage.py runserver 0.0.0.0:8000