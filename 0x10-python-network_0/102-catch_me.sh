#!/bin/bash
# script that makes request to 0.0.0.0:5000/catch_me
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: You got me!" --data "user_id=98"
