FROM python:3.11

COPY --from=openjdk:11-jre-slim /usr/local/openjdk-11 /usr/local/openjdk-11

ENV JAVA_HOME /usr/local/openjdk-11

RUN update-alternatives --install /usr/bin/java java /usr/local/openjdk-11/bin/java 1

WORKDIR /app

ADD bibds.py /app

RUN pip install pycsp3

CMD ["python", "./bibds.py"]