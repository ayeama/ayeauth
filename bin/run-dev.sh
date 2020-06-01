#!/bin/bash

set -x

export JWT_PRIVATE_KEY=/home/alexander/devel/ayeauth/env/jwt.private
export JWT_PUBLIC_KEY=/home/alexander/devel/ayeauth/env/jwt.public

ayeauth run --debug
