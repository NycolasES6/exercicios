
print("\n--- ---")
conjunto = {"Nycolas Ramos", "Atylas", "São Paulo"}
print(conjunto)

conjunto_num = {0, 2, 5}

print("\n--- ---")
conjunto.update(conjunto_num)
print(conjunto)

print("\n--- ---")
conjunto.update(("tupla", "testTupla", 25))
print(conjunto)

# No remove temos que especificar qual valor queremos retirar
print("\nremove --- ---")
print(conjunto)
conjunto.remove("tupla")
print(conjunto)

# No pop ele deleta um elemento aleatorio
print("\npop --- ---")
print(conjunto)
conjunto.pop()
print(conjunto)

print("\ndir --- ---")
print(dir(conjunto))

print("\ndiscard --- ---")
print(conjunto)
conjunto.discard("São Paulo")
print(conjunto)

print("\nclear --- ---")
print(conjunto)
conjunto.clear()
print(conjunto)

del conjunto
