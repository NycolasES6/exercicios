# Em python nao atribuimos o tipo a variavel, ele mesmo inseri o tipo no momento da atribuicao.
# A variavel nao pode comecar com numeros e simbolos, apenas letras.
# altura, Altura e ALTURA sao variaveis diferentes

x = 5
y = 3.5
z = 1+2j

w = 'Ana'
w = "Ana"

# Podemos adicionar o valor nas variaveis em sequencia
a, b, c = 1, 2, 3
print(a,b,c,)

a = b = c = "Nycolas"
print(a, b, c)

# string + string = string - CONCATENA
# numero + string = string - ERRO, nao podemos juntar variaveis de tipos diferentes
# numero + numero = numero - SOMA
print(a + w)
print(x+y)
print(w + x)

