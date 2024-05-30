from categoria import Categoria


class Transacao:
    def __init__(self, descricao: str, valor: float, categoria: Categoria):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria

    def exibir(self):
        print(f"DESCRICAO: {self.categoria} | VALOR: {self.valor} | DESCRICAO: {self.descricao}")


