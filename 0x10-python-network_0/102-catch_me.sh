#!/bin/bash
# script makes request to 0.0.0.0:5000/catch_me
curl -sLX PUT 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool" --data "user_id=98"
