
from clases import (
    SensorTemperatura,
    SensorHumedad,
    SensorMovimiento,
    SistemaSensores
)

def main():
    sistema = SistemaSensores()

    print("=== SISTEMA DE SENSORES ===")

    sistema.agregar(SensorTemperatura(25))
    sistema.agregar(SensorHumedad(55))
    sistema.agregar(SensorMovimiento(1))

    reporte = sistema.reporte()

    print("\n--- REPORTE CONSOLIDADO ---")
    print(f"Valor mínimo: {reporte['min']}")
    print(f"Valor máximo: {reporte['max']}")
    print(f"Promedio: {reporte['promedio']:.2f}")

if __name__ == "__main__":
    main()
