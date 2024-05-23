#!/bin/bash

var="nef892na9s1p9asn2aJs71nIsm"

for counter in {1..40}
do
    var=$(echo "$var" | base64)

    num="${#var}" # "#var" representa o número de caracteres da variavel var 
    
    echo "$counter - $num "

done