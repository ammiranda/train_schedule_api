FROM python:3.9.8
RUN apt-get -y update
RUN apt-get install -y build-essential
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "flask" ]
CMD [ "run", "--host=0.0.0.0" ]