class Cliente:
    def __init__(self, id=None, nombre="", apellido="", telefono="", email=""):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"[{self.id}] {self.nombre} {self.apellido} - {self.telefono} - {self.email}"



