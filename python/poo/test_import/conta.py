from categoria import Categoria

class Conta:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.categoria = Categoria("Alimentação")
