#            0                 1             2           3
times = ["Chicago Bulls", "Miami Heat", "Cleveland", "Lakers"]
#           -4                -3            -2          -1

num_int = [2, 3, 5, 7, 11, 13, 19]

num_float = [2.3, 5.6, 1.9, 3.2]

verdade = [True, False, False, True]

misturado = [True, "Nycolas", 3, 4.5]

print(type(misturado))

print("--- ---")

print(misturado)

print("--- ---")

print(times[2])

print("--- ---")

print(times[-4])

print("--- ---")

# :: retorna todos os indexes todos os elementos.
print(times[::])

print("--- ---")

# Vai imprimir do index que destacamos até o último.
print(times[2:])

# Vai imprimir do inicio até o index que destacamos -1.
print(times[:4])

# Vai imprimir o do primeiro index que destacamos até o ultimo index que destacamos -1.
print(times[2:4])

