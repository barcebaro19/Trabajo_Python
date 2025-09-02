import mysql.connector.pooling
from mysql.connector import Error

# Configuración de la base de datos
dbconfig = {
    "host": "localhost",
    "user": "root",
    "passwd": "",
    "database": "persona"
}

# Variable global para el pool
pool = None

def inicializar_pool():
    """Inicializa el pool de conexiones"""
    global pool
    try:
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool",
            pool_size=5,       # número de conexiones simultáneas
            **dbconfig
        )
        print("Pool de conexiones creado exitosamente")
        return True
    except Error as e:
        print(f"Error al crear el pool: {e}")
        return False

def get_connection():
    """Obtiene una conexión del pool"""
    global pool
    try:
        if pool is None:
            if not inicializar_pool():
                return None
        return pool.get_connection()
    except Error as e:
        print(f"Error al obtener conexión del pool: {e}")
        return None

# Inicializar el pool al importar el módulo
if __name__ == "__main__":
    inicializar_pool()
else:
    # Inicializar el pool cuando se importa como módulo
    inicializar_pool()
