from main import get_connection

try:
    conexion = get_connection()
    if conexion.is_connected():
        print("✅ Conexión obtenida desde el pool")

        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM cliente;")
        resultado = cursor.fetchall()
        for fila in resultado:
            print(fila)

except Exception as e:
    print(f"❌ Error al conectar a la base de datos: {e}")
finally:
    if cursor: cursor.close()
    if conexion: conexion.close()   # regresa conexión al pool
    print("🔒 Conexión liberada al pool")
