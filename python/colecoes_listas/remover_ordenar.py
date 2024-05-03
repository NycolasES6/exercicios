print("\nlista --- ---")
times = ["Chicago Bulls", "Miami Heat", "Lakers", "Utah Jazz", "Maverycks", "a teste", "Nuggets", "Golden State", "Cleveland"]
print(times)

# O pop deleta o ultimo elemento de uma lista.
print("\n.pop() --- ---")
times.pop()
print(times)

# O remove deleta o elemento especificado pelo valor.
print("\n.remove() --- ---")
times.remove("Chicago Bulls")
print(times)

# O sort organiza os elementos em ordem crescente, tanto números quanto letras.
print("\n.sort() --- ---")
times.sort()
print(times)

# O sort organiza os elementos em ordem crescente, tanto números quanto letras.
# Mas em questão das letras, ele separa em CASE, para evitarmos isto, temos de tratar.
print("\n.sort(key = str.lower) --- ---")
times.sort(key=str.lower)
print(times)

# O sort organiza os elementos em ordem decrescente, tanto números quanto letras.
print("\n.sort(reverse=True) --- ---")
times.sort(reverse=True)
print(times)

# O reverse inverte a ordem dos elementos.
print("\n.reverse() --- ---")
times.reverse()
print(times)

# O clear vai limpar a lista.
print("\nlista.clear() --- ---")
times.clear()
print(times)

# O del vai deletar a lista da execução do código.
print("\ndel lista --- ---")
del times
