from datetime import date


class Pessoa:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

    def diasVividos(self):
        return (date.today() - self.data_nascimento).days

Lucas = Pessoa("Lucas", date(2000, 9, 30))

print(Lucas.diasVividos())