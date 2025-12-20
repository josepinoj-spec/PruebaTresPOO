from clases import Auto, Moto, Camion, Estacionamiento

def main():
    estacionamiento = Estacionamiento()

    print("=== TARIFICADOR DE ESTACIONAMIENTO ===")

    for i in range(3):
        print(f"\nVehículo {i + 1}")
        patente = input("Patente: ")
        tipo = input("Tipo (auto/moto/camion): ").lower()
        minutos = int(input("Minutos estacionado: "))

        if tipo == "auto":
            estacionamiento.registrar(Auto(patente, minutos))
        elif tipo == "moto":
            estacionamiento.registrar(Moto(patente, minutos))
        elif tipo == "camion":
            estacionamiento.registrar(Camion(patente, minutos))
        else:
            print("Tipo inválido")

    print("\n--- REPORTE ---")
    print(f"Total recaudado: ${estacionamiento.total_recaudado()}")

if __name__ == "__main__":
    main()

