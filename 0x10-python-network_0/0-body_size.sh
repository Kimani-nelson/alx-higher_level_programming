#!/bin/bash
# This script takes in a URL, sends a request to that URL using curl,
# and displays the size of the body of the response in bytes

URL=$1
SIZE=$(curl -sI "$URL" | grep -i Content-Length | awk '{print $2}')
echo "$SIZE"

