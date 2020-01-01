FROM python:3.7

ARG VENDOR
ARG BUILD_DATE
ARG GIT_REPO
ARG VCS_REF
ARG VERSION
ARG TITLE="greeter-service"
ARG DESCRIPTION="PoC that returns a greeting like 'Hello' for 'Hello world'"
ARG DOCUMENTATION
ARG AUTHOR
ARG LICENSE="MIT"
LABEL org.opencontainers.image.created="${BUILD_DATE}" \
    org.opencontainers.image.url="${GIT_REPO}" \
    org.opencontainers.image.source="${GIT_REPO}" \
    org.opencontainers.image.version="${VERSION}" \
    org.opencontainers.image.revision="${VCS_REF}" \
    org.opencontainers.image.vendor="${VENDOR}" \
    org.opencontainers.image.title="${TITLE}" \
    org.opencontainers.image.description="${DESCRIPTION}" \
    org.opencontainers.image.documentation="${DOCUMENTATION}" \
    org.opencontainers.image.authors="${AUTHOR}" \
    org.opencontainers.image.licenses="${LICENSE}"

RUN pip3 install pipenv

WORKDIR /usr/src/app

COPY Pipfile ./
COPY Pipfile.lock ./

RUN set -ex && pipenv install --deploy --system

COPY . .

EXPOSE 5002

CMD [ "gunicorn", "-b0.0.0.0:5002", "wsgi:app" ]
