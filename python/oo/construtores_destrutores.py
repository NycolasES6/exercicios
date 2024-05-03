class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Deletando objeto...")

    def falar(self):
        print("Auau")

    def criar_cachorro(self):
        c = Cachorro("Zeus", "Branco e preto", False)
        print(c.nome)


c = Cachorro("Chappie", "Rosa")
c.falar()

print("Olá mundo")

del c

print("Olá mundo")
print("Olá mundo")
print("Olá mundo")
