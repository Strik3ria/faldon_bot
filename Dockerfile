FROM python:3.10-slim
LABEL maintainer="Robert Coones"

ENV RUN_USER bot
ENV RUN_GROUP bot
ENV RUN_UID 2002
ENV RUN_GID 2002

WORKDIR /opt/app

COPY faldon_bot.py faldon_bot.py
COPY launcher.py launcher.py
COPY cogs/ cogs/
COPY requirements.txt requirements.txt
COPY .env .env

RUN python -m pip install -r requirements.txt

RUN groupadd --gid ${RUN_GID} ${RUN_GROUP} \
    && useradd --uid ${RUN_UID} --gid ${RUN_GID} --home-dir /opt/app --shell /bin/bash ${RUN_USER} \
    && chown -R ${RUN_USER}:${RUN_GROUP} /opt/app

USER bot

CMD ["python", "launcher.py"]
