FROM python:3

MAINTAINER Jeeva S. Chelladhurai

RUN pip install flask

COPY src /src/

EXPOSE 5000

ENTRYPOINT ["python", "/src/app.py"]
