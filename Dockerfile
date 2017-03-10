# python:alpine is 3.{latest}
FROM python:alpine 

MAINTAINER Jeeva S. Chelladhurai

RUN pip install flask

COPY src /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
