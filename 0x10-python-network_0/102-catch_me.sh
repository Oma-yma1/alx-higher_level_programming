#!/bin/bash
# script that makes request to 0.0.0.0:5000/catch_me
curl -sL 0.0.0.0:5000/catch_me -X PUT -H "Origin: You got me!"