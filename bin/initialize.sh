#!/bin/bash

# initialize database
ayeauth database initialize

# create an admin user
ayeauth database model User post --username admin --password admin
