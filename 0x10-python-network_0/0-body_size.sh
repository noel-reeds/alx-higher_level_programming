#!/usr/bin/bash
# displays the size of the body response.
curl -sI "$1" | grep -i 'Content-Length' | cut -d' ' -f2
