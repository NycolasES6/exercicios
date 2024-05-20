from random import choice

escolhas = ["PEDRA", "PAPEL", "TESOURA"]
escolhas_perd = ["TESOURA", "PEDRA", "PAPEL"]


pontos_jogador = 0
pontos_maquina = 0


"""Escolha da maquina"""


def escolha_maquina():
    return choice(["PEDRA", "PAPEL", "TESOURA", "PAPEL", "PEDRA", "TESOURA"])


"""Escolha do jagador"""


def escolha_jogador():
    escolha = input("\n \n Qual a sua escolha ? \n - PEDRA \n - PAPEL \n - TESOURA \n ? ")
    escolha = escolha.upper()

    while escolha not in escolhas:
        print("Escolha inválida !! \n")
        escolha = input("\n\n Qual a sua escolha ? \n - PEDRA \n - PAPEL \n - TESOURA \n ? ")
        escolha = escolha.upper()

    return escolha


"""Confere o resultado da partida"""


def confere_resultado(escolha_do_jogador, escolha_da_maquina):
    for key, esc in enumerate(escolhas):
        if escolha_do_jogador == esc and escolha_da_maquina == escolhas_perd[key]:
            global pontos_jogador
            pontos_jogador += 1
            return "O jogador venceu"
        elif escolha_do_jogador == escolha_da_maquina:
            return "Empate"
        else:
            global pontos_maquina
            pontos_maquina += 1
            return "A maquina venceu"


"""Retorna o placar da partida"""


def mostra_placar():
    return f"\nPlacar - - - - - \n Jogador - {pontos_jogador} \n Máquina - {pontos_maquina}\n\n"


quer_jogar = True

while quer_jogar:
    quer_jogar = input("Quer jogar comigo ? \n [ s ] - SIM \n [ n ] - NAO \n ? ").upper()

    if quer_jogar in ["S", "SIM"]:
        quer_jogar = True
    else:
        quer_jogar = False
        print(mostra_placar())
        print("Ficou com medo ?")
        break

    print("A partida começou -----------------")
    escolha_do_jogador = escolha_jogador()
    escolha_da_maquina = escolha_maquina()

    print(f"A escolha do jogador foi {escolha_do_jogador}")
    print(f"A escolha da maquina foi {escolha_da_maquina}")

    print(f"\n{escolha_do_jogador} X {escolha_da_maquina}")
    print(f"\n{confere_resultado(escolha_do_jogador, escolha_da_maquina)}")

    print(mostra_placar())
