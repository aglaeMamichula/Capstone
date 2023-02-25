FROM pypy:latest
WORKDIR .
COPY . /
EXPOSE 5000
RUN pip install -r requirements.txt  

CMD python manage.py runserver 0.0.0.0:8000