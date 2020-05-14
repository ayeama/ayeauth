#!/bin/bash

set -x

# initialize database
ayeauth database initialize

# create default scopes
USERNAME_SCOPE=$(ayeauth database model Scope post --name "Username" --description "View your username")
ROLES_SCOPE=$(ayeauth database model Scope post --name "Roles" --description "View your roles")

# create default roles
ADMIN_ROLE=$(ayeauth database model Role post --name admin --description "Default administrator role")
USER_ROLE=$(ayeauth database model Role post --name user --description "Default user role")

# create default users
ADMIN_USER=$(ayeauth database model User post --username admin --password admin)
