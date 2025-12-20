from abc import ABC, abstractmethod

class Sensor(ABC):
    def __init__(self, valor):
        self._valor = valor

    @abstractmethod
    def normalizar(self):
        pass

    @abstractmethod
    def validar(self):
        pass


class SensorTemperatura(Sensor):
    def normalizar(self):
        return self._valor  # Celsius

    def validar(self):
        return -50 <= self._valor <= 100


class SensorHumedad(Sensor):
    def normalizar(self):
        return self._valor  # %

    def validar(self):
        return 0 <= self._valor <= 100


class SensorMovimiento(Sensor):
    def normalizar(self):
        return int(self._valor)

    def validar(self):
        return self._valor in (0, 1)


class SistemaSensores:
    def __init__(self):
        self._sensores = []

    def agregar(self, sensor):
        if sensor.validar():
            self._sensores.append(sensor)

    def reporte(self):
        valores = [s.normalizar() for s in self._sensores]
        return {
            "min": min(valores),
            "max": max(valores),
            "promedio": sum(valores) / len(valores)
        }

