#!/bin/bash
# takes in a URL as an arg, sends a GET request to the URL
curl -sX GET "$1" -H "XX-School-User-Id:98"
