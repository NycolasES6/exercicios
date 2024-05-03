
numero = int(input("Escolha um número para saber se ele é par ou ímpar: "))
teste = numero % 2

if bool(teste) : print(f"O número {numero} é ímpar")
else : print(f"O número {numero} é par")
