def imprimir_nome(nome=None, sobrenome="Seu sobrenome", idade=0):
    if nome != None:
        print("nome:", nome)
        print("sobrenome:", sobrenome)
        print("idade:", idade)
        print("-----" * 3)
    else:
        print("Por favor preencha os seus dados.")
        print("-----" * 3)


imprimir_nome(nome="Nycolas", idade=45)

imprimir_nome(idade=45)
