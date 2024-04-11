#!/bin/bash
# sends a GET request to return body of the response
curl -s -w "%{http_code}" "$1" | grep -q "200" && curl -s "$1"
