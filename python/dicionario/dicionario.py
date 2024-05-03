
# Listas - Coleção ordenada, mutável e que permite valores duplicados.
# Tuplas - Coleção ordenada, imutável e que permite valores duplicados.
# Dicionario - Coleção não ordenada, mutável e que não permite valores duplicados.

# index     0         1         2         3
lista = ["valor1", "valor2", "valor3", "valor2"]
tupla = ("valor1", "valor2", "valor3", "valor2")

# chave:valor
print("\n--- --- ---")
dicio = {"chave1" : "Nycolas", "chave2" : 25, "chave3" : "Gabriel", "chave4" : True}

print("\n--- --- ---")
print(dir(dicio))

print("\n--- --- ---")
print(f"\n{dicio}")

print("\n--- --- ---")
print(f"\n{dicio['chave4']}")

print("\n--- --- ---")
print(f"\n{len(dicio)}")

print("\n--- --- ---")
print(f"\n{dicio.keys()}")

print("\n--- --- ---")
print(f"\n{dicio.values()}")
