total = 350
num_saques = 0
movimentacoes =[]

def escolha():
    operacao = input("""Qual operação gostaria de fazer ?
        [1] - Depósito
        [2] - Saque
        [3] - Ver extrato
        [4] - Sair
    """)
    
    if operacao.isnumeric() :
        operacao = int(operacao)
        if operacao == 1:
            deposito()
        if operacao == 2:
            saque()
        if operacao == 3:
            extrato()
        if operacao == 4:
            pass
    else:
        print("\nDigite um número válido.\n")
        escolha()


def deposito():
    global total, movimentacoes
    val_deposito = input("""Qual valor gostaria de depositar: """)
    
    if val_deposito.isnumeric() :
        val_deposito = int(val_deposito)

        if val_deposito <= 0:
            print("\nDigite um valor maior que 0\n")
            deposito()

        total = total + val_deposito
        movimentacoes.append(f"Deposito: R${val_deposito:.2f}")
    else:
        print("\nDigite um valor válido.\n")
        escolha()

    escolha()


def saque():
    global total, num_saques, movimentacoes

    if num_saques >= 4:
        print("Limite diário de saque atingido.")
        escolha()

    val_saque = input("""Qual valor gostaria de sacar: """)
    
    if val_saque.isnumeric() :
        val_saque = int(val_saque)

        if val_saque > 500 :
            print("\nSaque máximo de R$500.00\n")
            saque()
        elif val_saque > total:
            print("\nSaldo insuficiente.\n")
            escolha()

        if val_saque <= 0:
            print("\nDigite um valor maior que 0\n")
            saque()

        total = total - val_saque
        num_saques+=1
        movimentacoes.append(f"Saque: R${val_saque:.2f}")
    else:
        print("\nDigite um valor válido.\n")
        saque()

    escolha()

def extrato():
    global total

    for value in movimentacoes:
        print(value)

    print(f"""- - - - - - - - - - - -
              Saldo total: R${total:.2f}
          """)

    escolha()

escolha()
