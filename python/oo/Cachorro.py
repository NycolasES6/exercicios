class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")

    def dormir(self):
        if self.acordado:
            self.acordado = False
            print("Zzzzz...")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"


cachorro_1 = Cachorro("Mussum", "Preta", True)

cachorro_1.latir()
cachorro_1.dormir()

print(cachorro_1.__str__())
