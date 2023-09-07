# syntax=docker/dockerfile:1
FROM python:3.10.13-slim-bullseye
EXPOSE 8080
EXPOSE 80
EXPOSE 9
WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
CMD ["python","./app.py"]
# CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]