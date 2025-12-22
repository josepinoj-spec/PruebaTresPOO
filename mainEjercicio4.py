
from clases.sensortemperatura import SensorTemperatura
from clases.sensorhumedad import SensorHumedad
from clases.sensormovimiento import SensorMovimiento
from clases.sistema_iot import SistemaIoT

sistema = SistemaIoT()

temp = SensorTemperatura()
hum = SensorHumedad()
mov = SensorMovimiento()

sistema.registrar_sensor(temp)
sistema.registrar_sensor(hum)
sistema.registrar_sensor(mov)

# Lecturas simuladas
temp.registrar_lectura(25, "C")
temp.registrar_lectura(77, "F")
temp.registrar_lectura(-10, "C")

hum.registrar_lectura(45)
hum.registrar_lectura(80)
hum.registrar_lectura(110)  # inválida

mov.registrar_lectura(3)
mov.registrar_lectura(7)
mov.registrar_lectura(0)

sistema.generar_reporte()
