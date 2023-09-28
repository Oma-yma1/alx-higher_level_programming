#!/bin/bash
# script takes in a URL, sends request to URL,displays the size of body
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2
