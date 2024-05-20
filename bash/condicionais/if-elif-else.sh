#!/bin/bash

value=$1

if [ $value -gt "10" ]

then
    echo "O número $value é maior do que 10"
elif [ $value -lt "10" ]
then
    echo "O número $value é menor do que 10"
else
    echo "$value não é um número"
fi