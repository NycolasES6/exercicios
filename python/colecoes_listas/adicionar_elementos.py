print("\nlista --- ---")
times = ["Chicago Bulls", "Miami Heat"]
print(times)

# O splite pega uma string e cria uma lista de acordo com o character de separação especificado.
print("\n.split() --- ---")
print("Nycolas Ramos".split(" "))

# O metodo append adiciona um elemento ao final da lista.
print("\n.append() --- ---")
times.append("Lakers")
print(times)

# O metodo insert insere um valor em um index especificado.E empurra os elementos
# para o index seguinte.
print("\n.insert() --- ---")
times.insert(0, "Nuggets")
print(times)

# Com o método extend podemos adicionar mais de um elemento de uma vez
# ao final do array.
print("\n.extend() --- ---")
times.extend(["Nets", "Maverycks", "Utah Jazz"])
print(times)
