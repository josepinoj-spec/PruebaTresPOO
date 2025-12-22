from clases.tarjeta import Tarjeta
from clases.transferencia import Transferencia
from clases.billeteradigital import BilleteraDigital
from clases.venta import Venta
from clases.tienda import Tienda

tienda = Tienda()
id_venta = 1

while True:
    print("\n--- MENÚ DE PAGOS ---")
    print("1. Tarjeta")
    print("2. Transferencia")
    print("3. Billetera Digital")
    print("4. Reporte final y salir")

    opcion = input("Seleccione medio de pago: ")

    if opcion == "4":
        break

    monto = int(input("Ingrese monto de la venta: "))

    if opcion == "1":
        cupo = int(input("Ingrese cupo disponible: "))
        medio = Tarjeta(cupo)

    elif opcion == "2":
        confirmada = input("¿Transferencia confirmada? (s/n): ") == "s"
        medio = Transferencia(confirmada)

    elif opcion == "3":
        saldo = int(input("Ingrese saldo de billetera: "))
        medio = BilleteraDigital(saldo)

    else:
        print("Opción inválida")
        continue

    if not medio.validar(monto):
        print(" Pago rechazado")
        continue

    recargo = medio.calcular_recargo(monto)
    venta = Venta(id_venta, monto, medio.nombre, recargo)
    tienda.registrar_venta(venta)

    print(" Venta registrada")
    print(venta.comprobante())

    id_venta += 1

total, recargos, comprobantes = tienda.generar_reporte()

print("\n REPORTE FINAL")
print(f"Total recaudado: ${int(total)}")
print(f"Total de recargos: ${int(recargos)}")
print("Comprobantes:")
for c in comprobantes:
    print("-", c)

