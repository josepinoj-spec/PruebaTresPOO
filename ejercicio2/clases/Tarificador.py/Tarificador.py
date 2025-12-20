
from abc import ABC, abstractmethod
import math

class Vehiculo(ABC):
    def __init__(self, patente, minutos):
        self._patente = patente
        self._minutos = minutos

    def horas(self):
        return math.ceil(self._minutos / 60)

    @abstractmethod
    def calcular_tarifa(self):
        pass


class Auto(Vehiculo):
    def calcular_tarifa(self):
        return self.horas() * 1000


class Moto(Vehiculo):
    def calcular_tarifa(self):
        return self.horas() * 500


class Camion(Vehiculo):
    def calcular_tarifa(self):
        return self.horas() * 2000


class Estacionamiento:
    def __init__(self):
        self._registros = []

    def registrar(self, vehiculo):
        self._registros.append(vehiculo)

    def total_recaudado(self):
        return sum(v.calcular_tarifa() for v in self._registros)

