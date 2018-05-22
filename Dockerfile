 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code
 WORKDIR /code
 ADD requirements.txt /code/
 COPY bootstrap.sh /code/bootstrap.sh
 RUN chmod +x /code/bootstrap.sh
 RUN pip install -r requirements.txt
 ADD . /code/
