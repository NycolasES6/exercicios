# Tuplas
tupla = ("Nycolas", "Atylas", "Eryck", "Davi")

print("\n Essas são as informações de uma tupla --- --- ---\n")
print(dir(tupla))
print("\nEla não possui funções de apagar ou para adicionar elementos.\nA maior diferença entre listas e tuplas é que as tuplas são imutáveis.")

lista = list(tupla)
print(f"\n{lista}")

itens = ("item-1", "item-2", "3".isnumeric())

# Desestruturação
(x, y, z) = itens
print(f"\nx : {x}\ny : {y}\nz : {z}")

# Assim o x vai se referir ao primeiro e o y ao resto
(x, *y) = itens
print(f"\nx : {x}\ny : {y}")

# Assim o x vai se referir ao primeiro o z ao ultimo e o y ao resto
(x, *y, z) = itens
print(f"\nx : {x}\ny : {y}\nz : {z}")
