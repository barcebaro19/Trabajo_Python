#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Archivo de prueba para verificar la conexión a la base de datos
"""

from main import get_connection
from api_python.cliente_dao import ClienteDAO

def test_conexion():
    """Prueba la conexión a la base de datos"""
    print("🔍 Probando conexión a la base de datos...")
    
    try:
        conexion = get_connection()
        if conexion and conexion.is_connected():
            print("✅ Conexión exitosa a la base de datos")
            
            # Probar obtener información de la base de datos
            cursor = conexion.cursor()
            cursor.execute("SELECT DATABASE()")
            db_name = cursor.fetchone()[0]
            print(f"📊 Base de datos conectada: {db_name}")
            
            # Probar verificar si existe la tabla cliente
            cursor.execute("SHOW TABLES LIKE 'cliente'")
            tabla_existe = cursor.fetchone()
            
            if tabla_existe:
                print("✅ Tabla 'cliente' encontrada")
                
                # Contar registros
                cursor.execute("SELECT COUNT(*) FROM cliente")
                count = cursor.fetchone()[0]
                print(f"📊 Número de clientes en la tabla: {count}")
                
                # Mostrar estructura de la tabla
                cursor.execute("DESCRIBE cliente")
                estructura = cursor.fetchall()
                print("\n📋 Estructura de la tabla 'cliente':")
                for campo in estructura:
                    print(f"  - {campo[0]}: {campo[1]} ({campo[2]})")
                
            else:
                print("❌ Tabla 'cliente' no encontrada")
                print("💡 Debes crear la tabla primero")
                
            cursor.close()
            conexion.close()
            return True
            
        else:
            print("❌ No se pudo conectar a la base de datos")
            return False
            
    except Exception as e:
        print(f"❌ Error durante la prueba: {e}")
        return False

def test_operaciones_crud():
    """Prueba las operaciones básicas del CRUD"""
    print("\n🧪 Probando operaciones CRUD...")
    
    try:
        # Probar listar clientes
        print("📋 Probando listar clientes...")
        clientes = ClienteDAO.listar()
        print(f"✅ Lista obtenida: {len(clientes)} clientes")
        
        # Probar insertar un cliente de prueba
        print("\n📝 Probando insertar cliente...")
        from api_python.cliente import Cliente
        cliente_prueba = Cliente(
            nombre="Cliente_Prueba",
            apellido="Test",
            telefono="999999999",
            email="prueba@test.com"
        )
        ClienteDAO.insertar(cliente_prueba)
        
        # Probar listar nuevamente
        print("\n📋 Listando clientes después de insertar...")
        clientes_actualizados = ClienteDAO.listar()
        print(f"✅ Total de clientes: {len(clientes_actualizados)}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error durante las pruebas CRUD: {e}")
        return False

if __name__ == "__main__":
    print("🚀 INICIANDO PRUEBAS DEL SISTEMA")
    print("=" * 50)
    
    # Probar conexión
    if test_conexion():
        print("\n✅ PRUEBA DE CONEXIÓN EXITOSA")
        
        # Probar operaciones CRUD
        if test_operaciones_crud():
            print("\n✅ PRUEBAS CRUD EXITOSAS")
            print("\n🎉 El sistema está funcionando correctamente!")
            print("💡 Ahora puedes ejecutar 'python menu_crud.py' para usar el menú completo")
        else:
            print("\n❌ PRUEBAS CRUD FALLIDAS")
    else:
        print("\n❌ PRUEBA DE CONEXIÓN FALLIDA")
        print("💡 Verifica que:")
        print("   - MySQL esté ejecutándose")
        print("   - La base de datos 'persona' exista")
        print("   - El usuario 'root' tenga acceso")
        print("   - La tabla 'cliente' esté creada")
    
    print("\n" + "=" * 50)
