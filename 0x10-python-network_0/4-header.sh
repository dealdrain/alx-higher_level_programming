#!/bin/bash
# takes in a URL as an arg, sends a GET request to the URL
curl -sX GET "$1" -H "X-HolbertonSchool-User-Id:98"
