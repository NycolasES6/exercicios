from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")

    def desligar(self):
        print("Desligando a TV...")

    def marca(self):
        print("LG")


controle = ControleTV()
controle.ligar()
controle.desligar()
controle.marca()
