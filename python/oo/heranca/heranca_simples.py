class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print(f'Ligando motor')


class Motocicleta(Veiculo):
    def bozina(self):
        print('Biibii...')


class Carro(Veiculo):
    def bozina(self):
        print('BIIIIIIIIIIIII...')


class Caminhao(Veiculo):
    def __init__(self,cor, placa, numero_rodas, carregado):
        self.carregado = carregado
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def bozina(self):
        print('Booooommmmmmmm...')

    def esta_carregado(self):

        print(f"{'Sim,' if self.carregado else 'Não'} estou carregado")


# Objeto moto
#moto = Motocicleta(cor='red', placa="GHT58", numero_rodas=2)
#moto.ligar_motor()
#moto.bozina()
#
#print()
#
# Objeto carro
#carro = Carro(cor='azul', placa="GHR930", numero_rodas=4)
#carro.bozina()

#print()

# Objeto caminhao
caminhao = Caminhao(cor='cinza', placa="GLO48", numero_rodas=8, carregado=False)
caminhao.esta_carregado()
