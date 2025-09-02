from api_python.cliente_dao import ClienteDAO
from api_python.cliente import Cliente

nuevo = Cliente(nombre="Juan", apellido="Pérez", telefono="123456789", email="juan@test.com")
ClienteDAO.insertar(nuevo)



