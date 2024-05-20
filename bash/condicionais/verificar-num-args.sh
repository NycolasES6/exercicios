#!/bin/bash

if [ $# -eq 0 ]
then
    echo -e "Forneça 1 argumento."
    exit 1
elif [ $# -gt 1 ]
then
    echo -e "Forneça apenas 1 argumento."
    exit 1
else
    value=$1
    echo "O argumento passado foi $value"
fi

