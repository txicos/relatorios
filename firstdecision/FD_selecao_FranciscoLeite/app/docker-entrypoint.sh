#!/bin/bash

set -e

if [ -n "$1" ]; then
    exec "$@"
fi

