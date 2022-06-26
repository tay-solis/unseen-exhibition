# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8080
CMD ["gunicorn", \
    "--bind", "0.0.0.0:8080", \
    "--workers", "1", \
    "--threads", "8", \
    "--timeout", "0", \
    "unseen.wsgi:application"]
