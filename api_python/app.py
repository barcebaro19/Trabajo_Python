from dao.cliente_dao import ClienteDAO
from modelos.cliente import Cliente

print("🚀 Iniciando aplicación...")

# Insertar
nuevo = Cliente(nombre="Laura", apellido="Gómez", telefono="555888999")
ClienteDAO.insertar(nuevo)

# Listar
for c in ClienteDAO.listar():
    print(c)
