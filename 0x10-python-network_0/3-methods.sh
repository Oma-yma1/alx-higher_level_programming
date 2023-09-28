#!/bin/bash
# script that takes in a UR,displays all HTTP methods
curl -sI "$1" | grep "Allow:" | cut -f2- -d ""
