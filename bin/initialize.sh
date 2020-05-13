#!/bin/bash

set -x

# initialize database
ayeauth database initialize

# create default roles
ADMIN_ROLE=$(ayeauth database model Role post --name admin --description "Default administrator role")
USER_ROLE=$(ayeauth database model Role post --name user --description "Default user role")

# create default users
ADMIN_USER=$(ayeauth database model User post --username admin --password admin)
ayeauth database model User add-role --user-id "${ADMIN_USER}" --role-id "${ADMIN_ROLE}"
