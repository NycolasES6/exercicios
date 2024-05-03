conjunto1 = {1, 2, 3, 4, 5, "Nycolas"}
conjunto2 = {"Nycolas", "Atylas", "Davi", 2, 4, 5 }

print("\nunion --- ---")
conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)

# INTERSECTION faz a interseção(teoria dos conjuntos).

# O intersection devemos atribuir ele a uma variavel
print("\nintersection --- ---")
print(conjunto1.intersection(conjunto2))

# O intersection_update não devemos atribuir ele a uma variavel, ele é o método de um set
print("\nintersection_update --- ---")
conjunto1.intersection_update(conjunto2)
print(conjunto1)

print("\n difference --- ---")
conjunto4 = {1, 2, 3, 4, 5, 6}
conjunto5 = {1, 3, 5}
conjunto6 = conjunto4.difference(conjunto5)
print(conjunto6)

# symmetric_difference = difference
# symmetric_difference_update = difference_update