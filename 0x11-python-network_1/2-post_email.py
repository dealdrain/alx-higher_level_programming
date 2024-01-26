#!/usr/bin/python3
"""
 takes in a URL and an email, sends a POST request to the passed URL
"""


import urllib.parse as parse
import urllib.request as request
from sys import argv

if __name__ == "__main__":
    mailData = parse.urlencode({'email': argv[2]}).encode('utf-8')
    ReqData = request.Request(argv[1], mailData)
    with request.urlopen(ReqData) as Data:
        print(Data.read().decode('utf-8'))
