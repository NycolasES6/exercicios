numero = int(input("Qual o número de teste ? "))

if numero > 1 :
    for x in range(2, numero) :
        if numero % x == 0 :
            print("Número não primo.")
            break
else : print("Número menor ou igual á 1.")