print("Bom dia, qual o seu nome ?")
nome = input()
print(type(nome))

idade = input("\nQual a sua idade ? ")
print(type(idade))

idade = int(input("\nQual a sua idade ? "))
print(type(idade))

print("O seu nome é {0}, e a sua idde é {1}".format(nome, idade))

print(f"O seu nome é {nome}, e a sua idde é {idade}")