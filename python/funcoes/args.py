# def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None, *args):
#     print("-----" * 3)
#     print(nomeImovel)
#     print(n_quartos)
#     print(vagasGaragem)
#     print(args)


# """*args - Fica no formato de uma tupla"""

# imprimir_imovel("Valparaiso", 4, 5, "Nycolas Ramos", "Atylas", "Davi")


def imprimir_nomes(*nomes):
    print(nomes)

lista_nomes = ["Nycolas", "Atylas", "Pedro"]
imprimir_nomes(*lista_nomes)
