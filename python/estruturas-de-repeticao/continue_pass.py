# O break sai do laço de repetição.
for x in range(10) :
    if x == 3 : break
    print(x)

print("--- ---")

# O continue passa para a próxima iteração do laço.
for x in range(10) :
    if x == 3 : continue
    print(x)

print("--- ---")

# O pass é uma palavra que deve ser usada sempre que o programa requisitar sintaticamente que se preencha
# uma lacuna, como é o caso da definição de uma função: após a linha do def tem que haver algum conteúdo.

def soma_de_quadrados(x, y):
    pass # k = x**x + y**y
    # return k

# O código acima garante que, ainda que eu não esteja certo a respeito da função,
# ela possa existir e ser usada no resto do meu código, sem apresentar erros.

print("--- ---")
