FROM python:3.10-slim
LABEL maintainer="Robert Coones"

COPY faldon_bot.py /faldon_bot.py
COPY launcher.py /launcher.py
COPY cogs/ /cogs/
COPY requirements.txt /requirements.txt
COPY .env /.env

RUN python -m pip install -r requirements.txt

CMD ["python", "/launcher.py"]
