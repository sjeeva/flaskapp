FROM python:alpine # points to 3.latest 

MAINTAINER Jeeva S. Chelladhurai

RUN pip install flask

COPY src /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
