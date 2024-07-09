#!/bin/bash
# send GET request to a given URL with a header variable displayed
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
