#!/bin/bash
# displays the status code of response
curl -sI "$1" | grep 'HTTP' | cut -d' ' -f2