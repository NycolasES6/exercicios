#!/bin/bash
echo "Additional options available:"

echo -e "\t1) Identfy the corresponding network range of target domain."

echo -e "\t2) Ping discovered hosts."

echo -e "\t3) All checks"

echo -e "\t*) Exit.\n"


read -p "Select your option: " -r opt


case $opt in
    "1")
        echo "network_range"
    ;;

    "2")
        echo "ping_host"
    ;;

    "3")
        echo "network_range and ping_host"
    ;;

    "*") exit 0 ;;
esac

