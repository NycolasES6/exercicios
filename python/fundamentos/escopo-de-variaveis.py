# Variaveis locais sao acessiveis apenas no escopo em que foram declaradas, e tem preferencia dentro de eu escopo.
#Globais sao acessiveis em quaquer lugar do codigo.

a = "Nycolas" # Variavel global

def funcao():
    a = "Atylas" # Variavel local
    print(a) # Variavel local
funcao()

def funcaoG():
    print(a) # Variavel Global
funcaoG()

print(a) # Variavel Global