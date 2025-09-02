import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",   # usa 'passwd' porque así lo tienes en conector.py
            database="persona"
        )
        return conexion
    except Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
