#!/bin/bash

set -x

# generate JWT key pair
openssl genrsa -out "env/$KEY_NAME.private" 4096
openssl rsa -in "env/$KEY_NAME.private" -out "env/$KEY_NAME.public" -pubout -outform PEM

# install ayeauth
pip install -e .

# initialize ayeauth
ayeauth database delete
ayeauth database initialize
ADMIN_ROLE=$(ayeauth database model Role post --name admin --description "Default administrator role")
USER_ROLE=$(ayeauth database model Role post --name user --description "Default user role")
ADMIN_USER=$(ayeauth database model User post --username admin --password admin)
