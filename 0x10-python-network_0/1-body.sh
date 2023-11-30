#!/bin/bash
# This script takes in a URL, sends a GET request to the URL using curl,
# and displays the body of the response if the response status code is 200

URL=$1
STATUS_CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL" 2>/dev/null)

if [ "$STATUS_CODE" -eq 200 ]; then
    curl -s "$URL"
elif [ "$STATUS_CODE" -ge 400 ]; then
    echo "Error: HTTP $STATUS_CODE"
elif [ "$STATUS_CODE" = "000" ]; then
    echo "Error: Unexpected response code $STATUS_CODE"
else
    echo "Unexpected response: HTTP $STATUS_CODE"
fi

