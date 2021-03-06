FROM python:2.7
EXPOSE 5500
WORKDIR /app
COPY . /app

RUN chmod a+x .shipped/build .shipped/run .shipped/test

RUN [".shipped/build"]
CMD .shipped/run
