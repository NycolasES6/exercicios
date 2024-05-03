def characters(palavra: str):
    return len(palavra)

print(characters("Nycolas"))

# par impar

def par_impar(num : int):
    if num % 2 == 0 : return "Número é par"
    elif num % 2 == 1 : return "Número é ímpar"

num = input("Qual número você quer verificar se é par ou ímpar ? ")

if num.isnumeric() :
    num = int(num)
    print(par_impar(num))
else : print("Escolha um número válido.")