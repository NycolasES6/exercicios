maior_numero = 0
menor_numero = 0

for x in range(5) : 
    numero = int(input("Escolha um numero : "))
    if x == 0 : maior_numero, menor_numero = numero, numero
    
    if numero > maior_numero : maior_numero = numero
    if numero < menor_numero : menor_numero = numero

print(f"O maior número é {maior_numero} e o menor é {menor_numero}")