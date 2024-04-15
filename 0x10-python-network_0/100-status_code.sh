#!/bin/bash
# displays the status code of response
curl -sI "$1" -w "%{response_code}" -o /dev/null
