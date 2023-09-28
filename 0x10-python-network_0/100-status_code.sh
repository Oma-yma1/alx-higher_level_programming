#!/bin/bash
# script that sends a request to URL passed as argument
curl -s -o /dev/null -I --w "%{http_code}" "$1"
