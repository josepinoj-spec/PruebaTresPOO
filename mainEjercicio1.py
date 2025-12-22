
from clases.notificacion import Notificacion
form clases.canalcorreo import CanalCorreo
from clases.canalsms import CanalSMS
from clases.canalwebhook import CanalWebhook

class GestorNotificaciones:
    def __init__(self):
        self._canales = set()

    def registrar(self, canal):
        if canal in self._canales:
            print(" Canal duplicado, no se agrega.")
            return False
        if not canal.validar_destino():
            print(" Destino inválido para el canal.")
            return False
        self._canales.add(canal)
        print(" Canal agregado:", canal.destino)
        return True

    def enviar_a_todos(self, mensaje: str):
        if not isinstance(mensaje, str) or mensaje.strip() == "":
            raise ValueError("El mensaje no puede ser vacío.")
        resumen = {"exitos": 0, "fallos": 0, "costo": 0.0}
        for canal in self._canales:
            ok = canal.enviar(mensaje)
            resumen["costo"] += canal.costo(mensaje)
            if ok:
                resumen["exitos"] += 1
            else:
                resumen["fallos"] += 1
        return resumen

def demo():
    gestor = GestorNotificaciones()
    # Registrar varios destinos
    gestor.registrar(CanalCorreo("usuario@example.com"))
    gestor.registrar(CanalSMS("987654321"))
    gestor.registrar(CanalWebhook("https://api.miservicio.com/hooks/ABCDE12345"))

    # Envío de 2 mensajes distintos y mostrar resumen
    for msg in ["Hola equipo, alerta de mantenimiento.", "Mensaje muy largo " * 15]:
        try:
            r = gestor.enviar_a_todos(msg)
            print(f"\n Resumen para: '{msg[:30]}...'\n- Éxitos: {r['exitos']}\n- Fallos: {r['fallos']}\n- Costo total: {r['costo']:.2f}")
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    demo()
