#!/bin/bash
# Sends a GET request to the given URL and displays the body of a 200 status code response
curl -sL -w "%{http_code}" -o /dev/null "$1" | {
    read -r status
    if [ "$status" -eq 200 ]; then
        curl -s "$1"
    fi
}

