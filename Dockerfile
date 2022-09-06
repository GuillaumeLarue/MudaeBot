FROM python:3.9-slim

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./main.py .

CMD ["python3", "-u", "main.py", "-i", "discord_login", "-p", "discord_password"]
