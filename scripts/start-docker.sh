#!/bin/bash

start_cmd=$1
exit_code=0

docker compose pull

if [ -z "$start_cmd" ]; then
  docker compose up -d --wait
else
  eval "$start_cmd"
fi
