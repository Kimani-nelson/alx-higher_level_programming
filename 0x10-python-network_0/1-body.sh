#!/bin/bash
# This script takes in a URL, sends a GET request to the URL using curl,
# and displays the body of the response if the response status code is 200

URL=$1
BODY=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
if [ "$BODY" -eq 200 ]; then
    curl -s "$URL"
fi

