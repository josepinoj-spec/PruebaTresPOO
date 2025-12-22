from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__lecturas = []

    def registrar_lectura(self, valor, unidad=None):
        valor_normalizado = self.normalizar(valor, unidad)
        if self.validar(valor_normalizado):
            self.lecturas.append(valor_normalizado)

    def estadisticas(self):
        if not self.lecturas:
            return None, None, None

        minimo = min(self.lecturas)
        maximo = max(self.lecturas)
        promedio = sum(self.lecturas) / len(self.lecturas)
        return minimo, maximo, promedio

    @abstractmethod
    def normalizar(self, valor, unidad):
        pass

    @abstractmethod
    def validar(self, valor):
        pass


class SensorTemperatura(Sensor):
    def __init__(self):
        super().__init__("Temperatura (°C)")

    def normalizar(self, valor, unidad):
        if unidad == "F":
            return (valor - 32) * 5 / 9
        return valor  # Celsius

    def validar(self, valor):
        return -50 <= valor <= 100


class SensorHumedad(Sensor):
    def __init__(self):
        super().__init__("Humedad (%)")

    def normalizar(self, valor, unidad=None):
        return valor

    def validar(self, valor):
        return 0 <= valor <= 100


class SensorMovimiento(Sensor):
    def __init__(self):
        super().__init__("Movimiento (eventos)")

    def normalizar(self, valor, unidad=None):
        return int(valor)

    def validar(self, valor):
        return valor >= 0

    
class SistemaIoT:
    def __init__(self):
        self.sensores = []

    def registrar_sensor(self, sensor):
        self.sensores.append(sensor)

    def generar_reporte(self):
        print("\n REPORTE CONSOLIDADO DE SENSORES\n")

        for s in self.sensores:
            minimo, maximo, promedio = s.estadisticas()
            print(f"Sensor: {s.nombre}")

            if minimo is None:
                print("  Sin lecturas\n")
                continue

            print(f"  Mínimo: {minimo:.2f}")
            print(f"  Máximo: {maximo:.2f}")
            print(f"  Promedio: {promedio:.2f}\n")
