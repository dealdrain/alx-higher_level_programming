#!/bin/bash
# takes in a URL and displays all HTTP meths
curl -Is "$1" | grep Allow | cut -c 8-
