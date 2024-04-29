class Veiculo:
    def __init__(self, num_rodas, placa, num_farois, cor):
        self.num_rodas = num_rodas
        self.placa = placa
        self.num_farois = num_farois
        self.cor = cor

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join(
            [f'{chave}={valor}' for chave, valor in self.__dict__.items()]
        )}"


class Carro(Veiculo):
    def __init__(self, num_rodas, placa, num_farois, cor, cheio):
        self.cheio = cheio
        super.__init__(num_rodas, placa, num_farois, cor)

    def buzinar():
        print("BIIIIIIIIIIII BIIIIIIIIIII")


carro = Carro(4, "789jhj", 4, "Azul", False)
carro.__str__()
