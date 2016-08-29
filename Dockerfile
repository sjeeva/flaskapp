FROM python:3

MAINTAINER Jeeva S. Chelladhurai

RUN pip install flask

COPY src /src/

ENTRYPOINT ["python", "/src/app.py"]
