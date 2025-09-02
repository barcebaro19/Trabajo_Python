from main import get_connection
from api_python.cliente import Cliente
from mysql.connector import Error

class ClienteDAO:

    @staticmethod
    def insertar(cliente):
        try:
            conexion = get_connection()
            if conexion is None:
                print(" No se pudo obtener conexión")
                return
            cursor = conexion.cursor()
            # Corregido para coincidir con los nombres reales de las columnas
            sql = "INSERT INTO cliente (Nombre, Apellido, Telfono, email) VALUES (%s, %s, %s, %s)"
            valores = (cliente.nombre, cliente.apellido, cliente.telefono, cliente.email)
            cursor.execute(sql, valores)
            conexion.commit()
            print("Cliente insertado correctamente")
        except Exception as e:
            print(f"Error al insertar cliente: {e}")
        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()  # libera al pool

    @staticmethod
    def listar():
        clientes = []
        try:
            conexion = get_connection()
            if conexion is None:
                print(" No se pudo obtener conexión")
                return clientes
            cursor = conexion.cursor()
            # Corregido para coincidir con los nombres reales de las columnas
            cursor.execute("SELECT id, Nombre, Apellido, Telfono, email FROM cliente")
            for fila in cursor.fetchall():
                clientes.append(Cliente(id=fila[0], nombre=fila[1], apellido=fila[2], telefono=fila[3], email=fila[4]))
        except Exception as e:
            print(f"Error al listar clientes: {e}")
        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
        return clientes

    @staticmethod
    def actualizar(cliente: Cliente):
        try:
            conexion = get_connection()
            if conexion is None:
                print(" No se pudo obtener conexión")
                return
            cursor = conexion.cursor()
            # Corregido para coincidir con los nombres reales de las columnas
            sql = "UPDATE cliente SET Nombre=%s, Apellido=%s, Telfono=%s, email=%s WHERE id=%s"
            cursor.execute(sql, (cliente.nombre, cliente.apellido, cliente.telefono, cliente.email, cliente.id))
            conexion.commit()
            print("Cliente actualizado correctamente")
        except Error as e:
            print(f"Error al actualizar cliente: {e}")
        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    @staticmethod
    def eliminar(id_cliente):
        try:
            conexion = get_connection()
            if conexion is None:
                print(" No se pudo obtener conexión")
                return
            cursor = conexion.cursor()
            sql = "DELETE FROM cliente WHERE id=%s"
            cursor.execute(sql, (id_cliente,))
            conexion.commit()
            print("Cliente eliminado correctamente")
        except Error as e:
            print(f"Error al eliminar cliente: {e}")
        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()

    @staticmethod
    def buscar_por_id(id_cliente):
        try:
            conexion = get_connection()
            if conexion is None:
                print(" No se pudo obtener conexión")
                return None
            cursor = conexion.cursor()
            # Corregido para coincidir con los nombres reales de las columnas
            sql = "SELECT id, Nombre, Apellido, Telfono, email FROM cliente WHERE id=%s"
            cursor.execute(sql, (id_cliente,))
            fila = cursor.fetchone()
            if fila:
                return Cliente(id=fila[0], nombre=fila[1], apellido=fila[2], telefono=fila[3], email=fila[4])
            else:
                print(f"No se encontró cliente con ID {id_cliente}")
                return None
        except Exception as e:
            print(f"Error al buscar cliente: {e}")
            return None
        finally:
            if cursor: cursor.close()
            if conexion: conexion.close()
