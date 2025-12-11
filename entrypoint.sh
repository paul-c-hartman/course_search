#!/bin/bash

cleanup_and_exit() {
    echo "Exiting cleanly"
    exit 0
}

trap cleanup_and_exit SIGINT SIGTERM SIGHUP

set -eo pipefail

# Just run until terminated
while true; do
    sleep 1
done