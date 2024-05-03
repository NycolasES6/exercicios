numero = int(input("De qual número vc quer obter o fatorial ? "))

fatorial = numero

if fatorial < 0 : print("Não existe fatorial de números negativos.")
elif fatorial == 0 : fatorial = 1
else :
    i = 0
    while (numero - i) != 1 :
        i = i + 1
        fatorial = fatorial * (numero - i)
    print(f"O fatorial de {numero} é {fatorial}")