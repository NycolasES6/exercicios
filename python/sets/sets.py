# Não ordenada, imutavel, não permite valores duplicados.
# Também conhecidos como conjuntos.

conjunto = {"Nycolas Ramos", False, 13, 17.5, "São Paulo"}

print("\n --- ---")
print(dir(conjunto))

print("\n --- ---")
print(conjunto)

print("\ntype --- ---")
print(type(conjunto))

print("\nlen --- ---")
print(len(conjunto))

print("\nconversao --- ---")
tupla = ("Nycolas Ramos", False, 13, 17.5, "São Paulo", "Eryck")
print(type(tupla))
novo_conjunto = set(tupla)
print(type(novo_conjunto))

print("\nfor --- ---")
for x in novo_conjunto:
    print(x)

print("\nin --- ---")
print("Nycolas Ramos" in novo_conjunto)
