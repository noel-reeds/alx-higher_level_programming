#!/bin/bash
# POST a JSON file
curl -s -H "Content-Type: application/json" -d "@$2" "$1"
