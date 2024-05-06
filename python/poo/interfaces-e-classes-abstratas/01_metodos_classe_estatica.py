class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p2 = Pessoa.criar_de_nascimento(1995, 8, 31, "João")
print(f"Idade:{p2.idade}\tNome:{p2.nome}")

print(Pessoa.e_maior_idade(12))
print(Pessoa.e_maior_idade(18))
