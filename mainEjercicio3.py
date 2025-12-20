from clases import Tarjeta, Transferencia, BilleteraDigital, Venta

def main():
    venta = Venta()

    print("=== SISTEMA DE PAGOS ===")

    for i in range(3):
        print(f"\nVenta {i + 1}")
        monto = float(input("Monto: "))
        medio = input("Medio (tarjeta/transferencia/billetera): ").lower()

        if medio == "tarjeta":
            pago = Tarjeta(monto)
        elif medio == "transferencia":
            pago = Transferencia(monto)
        elif medio == "billetera":
            pago = BilleteraDigital(monto)
        else:
            print("Medio inválido")
            continue

        if pago.validar():
            venta.registrar(pago)
            print(f"Pago aceptado. Total a pagar: ${pago.total():.0f}")
        else:
            print("Pago rechazado")

    print("\n--- REPORTE FINAL ---")
    print(f"Total recaudado: ${venta.total_recaudado():.0f}")

if __name__ == "__main__":
    main()

