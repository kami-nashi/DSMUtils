FROM python:3.6-alpine

RUN adduser -D dsmtools

WORKDIR /home/dsmtools

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY static static
COPY templates templates
COPY __init__.py calculators.py db_dump.py main.py requirements ./

RUN chmod +x main.py
RUN chown -R dsmtools:dsmtools ./
ENV FLASK_APP main.py

USER dsmtools

EXPOSE 5000
exec gunicorn -b :5000 --access-logfile - --error-logfile - main:app

ENTRYPOINT ["./boot.sh"]
