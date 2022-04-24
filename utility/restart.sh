#!/usr/bin/env bash

gunicorn=`ps -C gunicorn -o pid= | tail -n 1`
kill -HUP $gunicorn
