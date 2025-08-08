FROM python:3.12

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY req.txt /app/
RUN pip install --upgrade pip && \
    pip install -r req.txt

COPY nginx/nginx.conf /etc/nginx/conf.d/

COPY . /app/
FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    gettext \
    libpq-dev \
    curl \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /jashtar-kyimyly/

WORKDIR /jashtar-kyimyly

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#RUN gunicorn --version


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
