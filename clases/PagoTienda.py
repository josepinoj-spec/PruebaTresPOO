
from abc import ABC, abstractmethod

class PagoTiend(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre

    @abstractmethod
    def validar(self, monto):
        pass

    @abstractmethod
    def calcular_recargo(self, monto):
        pass


class Tarjeta(MedioPago):
    def __init__(self, cupo):
        super().__init__("Tarjeta")
        self.cupo = cupo

    def validar(self, monto):
        return monto <= self.cupo

    def calcular_recargo(self, monto):
        return monto * 0.05  # 5%
    


class Transferencia(MedioPago):
    def __init__(self, confirmada):
        super().__init__("Transferencia")
        self.__confirmada = confirmada

    def validar(self, monto):
        return self.confirmada

    def calcular_recargo(self, monto):
        return 0


class BilleteraDigital(MedioPago):
    def __init__(self, saldo):
        super().__init__("Billetera Digital")
        self.___saldo = saldo

    def validar(self, monto):
        return monto <= self.saldo

    def calcular_recargo(self, monto):
        return 500  # recargo fijo

class Venta:
    def __init__(self, id_venta, monto, medio_pago, recargo):
        self.__id_venta = id_venta
        self.__monto = monto
        self.__medio_pago = medio_pago
        self.__recargo = recargo

    def comprobante(self):
        total = self.monto + self.recargo
        return f"Venta {self.id_venta} | Medio: {self.medio_pago} | Total pagado: ${int(total)}"
    
class Tienda:
    def __init__(self):
        self.__ventas = []

    def registrar_venta(self, venta):
        self.ventas.append(venta)

    def generar_reporte(self):
        total = 0
        total_recargos = 0
        comprobantes = []

        for v in self.ventas:
            total += v.monto + v.recargo
            total_recargos += v.recargo
            comprobantes.append(v.comprobante())

        return total, total_recargos, comprobantes
    
    


