#!/bin/bash
# script takes in URL as argument, sends GET request to URL
curl -s -H "X-School-User-Id":98 "$1"
