class Animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(
            [f'{chave}={valor}' for chave, valor in self.__dict__.items()]
        )}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass


# gato = Gato(5, "Preto")
# print(gato.__str__())

orn = Ornitorrinco(num_patas=2, cor_pelo="Vermelho", cor_bico="Laranja")
print(orn.__str__())
