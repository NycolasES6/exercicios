#!/bin/bash

var="8dm7KsjU28B7v621Jls"

value="ERmFRMVZ0U2paTlJYTkxDZz09Cg"

for i in {1..40}
do
    var=$(echo "$var" | base64)

    # echo ${#var}

    if [[ $var =~ $value ]]
    then
        lastCharacters=$(echo "$var" | tail -c 20)
        echo -n "$lastCharacters"
    fi

    # if [ $var -ne $value ]
    # then
    #     echo "Chei"
    # fi

done