#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de debug para diagnosticar problemas de conexión
"""

import sys
import traceback

def debug_conexion():
    """Función para debuggear la conexión paso a paso"""
    print("🔍 INICIANDO DEBUG DE CONEXIÓN")
    print("=" * 50)
    
    try:
        print("1️⃣ Importando módulos...")
        from main import get_connection
        print("✅ main.py importado correctamente")
        
        from api_python.cliente_dao import ClienteDAO
        print("✅ ClienteDAO importado correctamente")
        
        print("\n2️⃣ Probando conexión...")
        conexion = get_connection()
        
        if conexion is None:
            print("❌ get_connection() retornó None")
            return False
            
        if not conexion.is_connected():
            print("❌ Conexión no está activa")
            return False
            
        print("✅ Conexión obtenida y activa")
        
        print("\n3️⃣ Probando consulta simple...")
        cursor = conexion.cursor()
        
        # Verificar si la base de datos existe
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()[0]
        print(f"📊 Base de datos actual: {db_name}")
        
        # Verificar si la tabla existe
        cursor.execute("SHOW TABLES LIKE 'cliente'")
        tabla_existe = cursor.fetchone()
        
        if not tabla_existe:
            print("❌ Tabla 'cliente' NO existe")
            cursor.close()
            conexion.close()
            return False
            
        print("✅ Tabla 'cliente' existe")
        
        # Contar registros
        cursor.execute("SELECT COUNT(*) FROM cliente")
        count = cursor.fetchone()[0]
        print(f"📊 Número de registros en tabla: {count}")
        
        if count == 0:
            print("⚠️ La tabla está vacía - no hay clientes registrados")
        else:
            print("✅ Hay clientes en la tabla")
            
            # Mostrar estructura
            cursor.execute("DESCRIBE cliente")
            estructura = cursor.fetchall()
            print("\n📋 Estructura de la tabla:")
            for campo in estructura:
                print(f"  - {campo[0]}: {campo[1]} ({campo[2]})")
            
            # Mostrar algunos registros
            cursor.execute("SELECT * FROM cliente LIMIT 3")
            registros = cursor.fetchall()
            print(f"\n📋 Primeros {len(registros)} registros:")
            for registro in registros:
                print(f"  {registro}")
        
        cursor.close()
        conexion.close()
        print("\n✅ Debug completado exitosamente")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR durante el debug: {e}")
        print("\n🔍 Traceback completo:")
        traceback.print_exc()
        return False

def debug_crud_operations():
    """Debug de las operaciones CRUD"""
    print("\n🧪 DEBUG DE OPERACIONES CRUD")
    print("=" * 50)
    
    try:
        from api_python.cliente_dao import ClienteDAO
        
        print("1️⃣ Probando listar clientes...")
        clientes = ClienteDAO.listar()
        print(f"📊 ClienteDAO.listar() retornó: {len(clientes)} clientes")
        
        if clientes:
            print("✅ Lista de clientes:")
            for i, cliente in enumerate(clientes, 1):
                print(f"  {i}. {cliente}")
        else:
            print("📭 No se obtuvieron clientes")
            
        return True
        
    except Exception as e:
        print(f"❌ Error en operaciones CRUD: {e}")
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🚀 INICIANDO DIAGNÓSTICO COMPLETO")
    print("=" * 60)
    
    # Debug de conexión
    conexion_ok = debug_conexion()
    
    if conexion_ok:
        print("\n✅ CONEXIÓN FUNCIONANDO - Probando CRUD...")
        crud_ok = debug_crud_operations()
        
        if crud_ok:
            print("\n🎉 TODO FUNCIONANDO CORRECTAMENTE")
        else:
            print("\n❌ PROBLEMA EN OPERACIONES CRUD")
    else:
        print("\n❌ PROBLEMA DE CONEXIÓN")
    
    print("\n" + "=" * 60)
    print("💡 Si hay errores, revisa:")
    print("   - MySQL esté ejecutándose")
    print("   - Base de datos 'persona' exista")
    print("   - Tabla 'cliente' esté creada")
    print("   - Usuario tenga permisos")
