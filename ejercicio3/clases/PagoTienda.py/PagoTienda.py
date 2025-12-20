
from abc import ABC, abstractmethod

class MedioPago(ABC):
    def __init__(self, monto):
        self._monto = monto

    @abstractmethod
    def validar(self):
        pass

    @abstractmethod
    def calcular_recargo(self):
        pass

    def total(self):
        return self._monto + self.calcular_recargo()


class Tarjeta(MedioPago):
    def validar(self):
        return self._monto <= 500000

    def calcular_recargo(self):
        return self._monto * 0.03


class Transferencia(MedioPago):
    def validar(self):
        return True

    def calcular_recargo(self):
        return 0


class BilleteraDigital(MedioPago):
    def validar(self):
        return self._monto <= 200000

    def calcular_recargo(self):
        return self._monto * 0.01


class Venta:
    def __init__(self):
        self._ventas = []

    def registrar(self, medio_pago):
        if medio_pago.validar():
            self._ventas.append(medio_pago)

    def total_recaudado(self):
        return sum(v.total() for v in self._ventas)

