
from clases.estacionamiento import Estacionamiento
from clases.auto import Auto
from clases.moto import Moto
from clases.camion import Camion

est = Estacionamiento()

datos = [
    Auto("AA1111", 480, 550),
    Moto("BB2222", 600, 650),
    Camion("CC3333", 700, 820),
    Auto("DD4444", 1080, 1200),
    Moto("EE5555", 1100, 1180),
    Camion("FF6666", 1000, 1130),
    Auto("GG7777", 300, 360),
    Moto("HH8888", 400, 460),
    Camion("II9999", 540, 660),
    Auto("JJ0000", 900, 980),
    Moto("KK1212", 1020, 1080),
    Camion("LL3434", 1140, 1260)
]

for v in datos:
    est.registrar(v)

total, top3, tipos = est.generar_reporte()

print(" REPORTE FINAL")
print(f"Total recaudado: ${total}")
print(f"Top 3 cobros más altos: {top3}")
print("Cantidad de vehículos por tipo:")
for t, c in tipos.items():
    print(f"- {t}: {c}")
