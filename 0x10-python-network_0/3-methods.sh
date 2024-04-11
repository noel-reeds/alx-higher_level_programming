#!/bin/bash
# displays all HTTP methods the server will accept
curl -sI OPTIONS "$1" | grep -i 'Allow' | cut -d' ' -f2-
