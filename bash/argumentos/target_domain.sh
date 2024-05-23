#!/bin/bash

if [ $# -eq 0 ]
then

    echo -e "Please, specift the domain. \n"
    echo -e "Usage:"
    echo -e "\t script.sh <domain>"
    exit 1

else

    domain=$1
    echo "You choose domain $domain "

fi