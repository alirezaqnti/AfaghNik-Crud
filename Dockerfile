FROM python3.11.8-alpine3.19

WORKDIR /app/project

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1
ENV PYTHONPATH=.
ENV CORESETTINGS_INDOCKER = true

RUN set -xe \
    && apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install virtualenvwrapper poetry==1.8.1 \
    && rm -rf /var/lib/apt/lists/*

COPY ["poetry.lock","pyproject.toml","./"]
RUN poetry install --no-root


COPY ["README.rst","Makefile","./"]
COPY core core
COPY local local

EXPOSE 8000

COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT [ "/entrypoint.sh" ]
