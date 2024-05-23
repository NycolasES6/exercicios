#!/bin/bash

if [ $# -eq 0 ]

then
    echo -e "Forneça algum argumento"
    exit 1
else
    domain=$1
    echo "$domain"
fi