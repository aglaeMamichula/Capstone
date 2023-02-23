FROM pypy:latest
WORKDIR .
COPY . /

RUN pip install -r requirements.txt  

CMD python manage.py runserver  