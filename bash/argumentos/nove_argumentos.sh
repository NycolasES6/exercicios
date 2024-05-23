#!/bin/bash

if [ $# -eq 0 ]
then
    echo -e "Forneça almenos 1 argumento"
    exit 1
elif [ $# -gt 9 ]
then
    echo -e "O máximo é de 9 argumentos"
    exit 1
fi