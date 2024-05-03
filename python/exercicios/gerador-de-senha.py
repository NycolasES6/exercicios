palavra_base = input("Qual a palavra base da senha ? ")
senha = ""

for letra in palavra_base:
    if letra in "Aa" : senha = senha + "@"
    elif letra in "Ee" : senha = senha + "&"
    elif letra in "Ii" : senha = senha + "!"
    elif letra in "Yy" : senha = senha + "|/"
    elif letra in "Oo" : senha = senha + "@"
    elif letra in "Uu" : senha = senha + "("
    elif letra in "Cc" : senha = senha + ")"
    else : senha = senha + letra

print(senha)