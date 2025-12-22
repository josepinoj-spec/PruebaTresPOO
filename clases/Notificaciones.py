from abc import ABC, abstractmethod


class Notificacion(ABC):
    """Clase abstracta base para todos los canales"""

    @abstractmethod
    def enviar(self, mensaje: str):
        pass

    @abstractmethod
    def validar_destino(self) -> bool:
        pass


class Correo(Notificacion):
    def __init__(self, email: str):
        self.email = email

    def validar_destino(self) -> bool:
        return "@" in self.email and "." in self.email

    def enviar(self, mensaje: str):
        print(f"Correo enviado a {self.email}: {mensaje}")


class MensajeSMS(Notificacion):
    def __init__(self, numero: str):
        self.numero = numero

    def validar_destino(self) -> bool:
        return self.numero.isdigit() and len(self.numero) >= 8

    def enviar(self, mensaje: str):
        print(f"SMS enviado a {self.numero}: {mensaje}")


class Webhook(Notificacion):
    def __init__(self, url: str):
        self.url = url

    def validar_destino(self) -> bool:
        return self.url.startswith("http")

    def enviar(self, mensaje: str):
        print(f"Webhook enviado a {self.url}: {mensaje}")
