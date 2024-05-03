#            0                 1             2           3         4        5
times = ["Chicago Bulls", "Miami Heat", "Cleveland", "Lakers", "Boston", "Nets"]
#           -6                 5            -4          -3        -2       -1

# Vai imprimir do index que destacamos até o último.
print(times[2:])

# Vai imprimir do inicio até o index que destacamos -1.
print(times[:4])

# Vai imprimir o do primeiro index que destacamos até o ultimo index que destacamos -1.
print(times[2:4])

# Vai imprimir o do primeiro index que destacamos até o ultimo index que destacamos -1 pulando de 1 em 1 no index.
print(times[2:4:1])

# Vai imprimir o do primeiro index que destacamos até o ultimo index que destacamos -1 pulando de 2 em 2 no index.
print(times[2:5:2])

# Nesse mesmo sentido podemos considerar uma string como uma lista e cada character é um elemento.
nome = "Nycolas"
print(nome[0:7:2])
