#!/bin/bash

# Equivale ao nome do script
echo Nome do Script: "$0"

# Equivale ao valor dos argumentos passados voa terminal
echo Argumentos passado: "$@"

# Equivale ao número de argumentos passados para o script
echo Numeros de argumentos passados: "$#"

# Equivale ao ID do processo atualmente em execução
echo ID do processo: "$$"

# Equivale ao status do script
echo Status do script: "$?"