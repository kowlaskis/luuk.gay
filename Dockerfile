# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

FROM python:3.10.10

WORKDIR /app

COPY . /app

# Expose the port that the application listens on.
EXPOSE 8007

RUN pip install -r requirements.txt

# Run the application.
CMD ["gunicorn", "-w 4", "-b :8007", "app:app"]
