from clases import Email, SMS, GestorNotificaciones

def main():
    gestor = GestorNotificaciones()

    print("=== SISTEMA DE NOTIFICACIONES ===")

    while True:
        tipo = input("Canal (email/sms/fin): ").lower()
        if tipo == "fin":
            break

        destino = input("Destino: ")

        if tipo == "email":
            gestor.agregar_canal(Email(destino))
        elif tipo == "sms":
            gestor.agregar_canal(SMS(destino))
        else:
            print("Canal inválido")

    mensaje = input("Mensaje a enviar: ")

    exitos, fallos, costo = gestor.enviar_mensaje(mensaje)

    print("\n--- RESUMEN ---")
    print(f"Envíos exitosos: {exitos}")
    print(f"Fallos: {fallos}")
    print(f"Costo total: ${costo}")

if __name__ == "__main__":
    main()

