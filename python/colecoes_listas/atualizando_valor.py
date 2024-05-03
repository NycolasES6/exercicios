print("\ntimes = []")
times = ["Chicago Bulls", "Miami Heat", "Cleveland", "Lakers"]
print(times)

print("\ntimes[0]")
times[0] = "Mavericks"
print(times)

print("\ntimes[1:3]")
times[1:3] = ["Golden State", "Utah Jazz"]
print(times)

# Se colocarmos um intervalo de 3 itens e passarmos apenas 1, ele
# ira substituir os 3 elementos por aquele que vc passou.

# Se colocarmos um intervalo de 3 itens a passar 5 elementos, ele ira substituir
# os 3 elementos por aqueles 5, e a lista terá 2 elementos a mais.
