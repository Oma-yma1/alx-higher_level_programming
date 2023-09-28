#!/bin/bash
# script that sends JSON POST request to URL
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
