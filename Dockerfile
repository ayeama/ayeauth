FROM python:3.8-slim-buster

LABEL maintainer="ayeama"
LABEL description="the ayeama authentication server"
LABEL version="0.1"

WORKDIR /usr/local/ayeauth

EXPOSE 5000

ENV JWT_PRIVATE_KEY=/usr/local/ayeauth/env/jwt.private
ENV JWT_PUBLIC_KEY=/usr/local/ayeauth/env/jwt.public

COPY . .
RUN pip install -e .
RUN mkdir env
RUN ./bin/install.sh

CMD ./bin/run.sh
