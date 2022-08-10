FROM python:3.9-slim

WORKDIR /usr/src/app

COPY ./main.py .
COPY ./requirements.txt .

#RUN sudo apt-get -y update
#RUN sudo apt-get install -y python3-pip
#RUN sudo apt-get install -y python3

RUN pip3 install -r requirements.txt

CMD ["python3", "-u", "main.py", "-i", "discord_login", "-p", "discord_password"]
