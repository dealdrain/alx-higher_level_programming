#!/bin/bash
#  takes in a URL, sends a request to that UR
curl -Is "$1" | grep Content-Length | cut -f2 -d' '
