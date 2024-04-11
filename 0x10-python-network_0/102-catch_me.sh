#!/bin/bash
# causes the server to respond with a custom message
curl -d "You got me!" -X PUT 0.0.0.0:5000/catch_me
