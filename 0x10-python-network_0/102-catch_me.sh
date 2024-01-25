#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond 
curl -sL -X PUT -H "Origin:HolbertonSchoo" -d "user_id=98" "0.0.0.0:5000/catch_me"
