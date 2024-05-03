# in Confere se um elemento está contido em outro
# not in Confere se um elemento nnao esta contido em outro

nome = "Nycolas"
nome_completo = "Nycolas Ramos dos Santos"
print("Esta contido") if  nome in nome_completo else print("Nao esta contido")
print("Esta contido") if  "x" in nome_completo else print("Nao esta contido")

# Arrays
array_nome = ["nycolas", "Atylas", "Eryck"]
print("Esta contido") if "nycolas" in array_nome else print("Nao esta contido")

print("Nao esta contido") if "Charles" not in array_nome else print("Esta contido")

