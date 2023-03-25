#!/bin/bash

# Check if the file exists
if [[ -f $1 ]]; then
  # Call the internal script and pass the file as an argument
  python3 ./main.py "$1"
else
  echo "File not found!"
  exit 1
fi
