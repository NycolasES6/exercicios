#def imprimir_nome(**nomes):
#    print(f"{nomes['nomes']} {nomes['sobrenomes']}")
#
#imprimir_nome(nomes="Ana", sobrenomes="Teixeira")

itens = []

for i in range(3):
    itens.append(input())

print("Lista de Equipamentos:")
for item in itens:
    print(f"- {item}")