class Veiculo():
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    
    def ligar_motor(self):
        print("Ligando motor")


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
    
    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado.")



caminhao_1 = Caminhao("Azul", "890-pooi", 6, True)
caminhao_1.ligar_motor()
caminhao_1.esta_carregado()

# moto = Motocicleta("preta", "abc-0978", 2)
# moto.ligar_motor()
