FROM pypy:latest
WORKDIR .
COPY . /

RUN pip install -r requirements.txt  
 
EXPOSE 8000  

CMD python manage.py runserver  