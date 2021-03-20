#!/usr/bin/env bash

ps -e
read -p "Enter PID: "
kill -HUP ${REPLY}
