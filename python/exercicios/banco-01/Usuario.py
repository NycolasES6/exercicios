class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Operacao:
    def __init__(self, valor, tipo, origem):
        self.valor = valor
        self.tipo = tipo
        self.origem = origem
        self.info = f"Valor: {valor}\nTipo: {tipo}\nOrigem: {origem}\n"


class Conta:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario
        self._saldo = 0
        self.extrato = []

    def get_saldo(self):
        print(self._saldo)

    def sacar(self, val_saque, origem):
        self._saldo -= val_saque
        self.extrato.append(Operacao(val_saque, "Saque", origem).info)

    def depositar(self, val_deposito, origem):
        self._saldo += val_deposito
        self.extrato.append(Operacao(val_deposito, "Saque", origem).info)

    def get_extrato(self):
        for var in self.extrato:
            print(var)


nycolas = Usuario("Nycolas", "088.565.765-23")

conta_n = Conta(nycolas)

conta_n.depositar(150, "Slário")

conta_n.depositar(250, "Slário")

conta_n.get_saldo()

conta_n.get_extrato()


