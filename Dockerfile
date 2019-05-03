FROM python:3.7

RUN mkdir -p /app/

WORKDIR /app

COPY requirements/base.pip .

RUN pip install --no-cache-dir -r base.pip

EXPOSE 80

CMD cd /app && sleep infinity