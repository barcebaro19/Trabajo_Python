from api_python.cliente_dao import ClienteDAO
from api_python.cliente import Cliente

cliente_editado = Cliente(id=1, nombre="Carlos", apellido="Ramírez", telefono="987654321")
ClienteDAO.actualizar(cliente_editado)


