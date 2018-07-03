FROM django:python2

ADD ./demo /demo
WORKDIR /demo

RUN pip install -r requirements.txt

#ensures the console.log lines are visible
ENV PYTHONUNBUFFERED=0 
EXPOSE 8080
ENTRYPOINT ["/bin/bash","-c","python /demo/manage.py runserver 0.0.0.0:8080"]
