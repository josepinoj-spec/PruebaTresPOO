from clases.Notificaciones import Correo, MensajeSMS, Webhook

class GestorNotificaciones:
    def __init__(self):
        self._canales = set()

    def registrar(self, canal):
        if canal in self._canales:
            print(" Canal duplicado, no se agrega.")
            return False

        if not canal.validar_destino():
            print(" Destino inválido.")
            return False

        self._canales.add(canal)
        return True

    def enviar_todos(self, mensaje: str):
        for canal in self._canales:
            canal.enviar(mensaje)


def main():
    gestor = GestorNotificaciones()

    correo = Correo("usuario@email.com")
    sms = MensajeSMS("987654321")
    webhook = Webhook("https://miapi.com/webhook")

    gestor.registrar(correo)
    gestor.registrar(sms)
    gestor.registrar(webhook)

    gestor.enviar_todos("Notificación de prueba")


if __name__ == "__main__":
    main()
