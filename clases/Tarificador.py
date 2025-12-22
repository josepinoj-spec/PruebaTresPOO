
from abc import ABC, abstractmethod
from math import ceil



class Tarificador(ABC):
    def __init__(self, patente, entrada, salida):
        self.__patente = patente
        self.__entrada = entrada
        self.__salida = salida

    def horas_estadia(self):
        minutos = self.salida - self.entrada
        return ceil(minutos / 60)

    def es_horario_punta(self):
        hora = self.entrada // 60
        return 18 <= hora < 21

    @abstractmethod
    def calcular_tarifa(self):
        pass
    
    
class Auto(Tarificador):
    TARIFA = 1500

    def calcular_tarifa(self):
        total = self.horas_estadia() * self.TARIFA
        if self.es_horario_punta():
            total *= 1.2
        return int(total)


class Moto(Tarificador):
    TARIFA = 800

    def calcular_tarifa(self):
        total = self.horas_estadia() * self.TARIFA
        if self.es_horario_punta():
            total *= 1.2
        return int(total)


class Camion(Tarificador):
    TARIFA = 3000

    def calcular_tarifa(self):
        total = self.horas_estadia() * self.TARIFA
        if self.es_horario_punta():
            total *= 1.2
        return int(total)


class Estacionamiento:
    def __init__(self):
        self.__estadias = []

    def registrar(self, vehiculo):
        self.estadias.append(vehiculo)

    def generar_reporte(self):
        total = 0
        cobros = []
        tipos = {}

        for v in self.estadias:
            cobro = v.calcular_tarifa()
            total += cobro
            cobros.append(cobro)

            tipo = type(v).__name__.lower()
            tipos[tipo] = tipos.get(tipo, 0) + 1

        top3 = sorted(cobros, reverse=True)[:3]

        return total, top3, tipos

