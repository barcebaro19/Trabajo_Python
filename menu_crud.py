#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Menú principal del CRUD de Clientes
Permite ejecutar todas las operaciones de forma interactiva
"""

from api_python.cliente_dao import ClienteDAO
from api_python.cliente import Cliente
import os

def limpiar_pantalla():
    """Limpia la pantalla del terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    """Muestra el menú principal"""
    print("=" * 50)
    print("           🗃️  CRUD DE CLIENTES 🗃️")
    print("=" * 50)
    print("1. 📝 Insertar nuevo cliente")
    print("2. 📋 Listar todos los clientes")
    print("3. 🔍 Buscar cliente por ID")
    print("4. ✏️  Actualizar cliente")
    print("5. 🗑️  Eliminar cliente")
    print("6. 🚪 Salir")
    print("=" * 50)

def insertar_cliente():
    """Función para insertar un nuevo cliente"""
    print("\n📝 INSERTAR NUEVO CLIENTE")
    print("-" * 30)
    
    try:
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        telefono = input("Teléfono: ").strip()
        email = input("Email: ").strip()
        
        if not nombre or not apellido:
            print("❌ El nombre y apellido son obligatorios")
            return
        
        nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, email=email)
        ClienteDAO.insertar(nuevo_cliente)
        
    except Exception as e:
        print(f"❌ Error al insertar: {e}")
    
    input("\nPresiona Enter para continuar...")

def listar_clientes():
    """Función para listar todos los clientes"""
    print("\n📋 LISTA DE CLIENTES")
    print("-" * 30)
    
    try:
        clientes = ClienteDAO.listar()
        if not clientes:
            print("📭 No hay clientes registrados")
        else:
            for cliente in clientes:
                print(f"  {cliente}")
    except Exception as e:
        print(f"❌ Error al listar: {e}")
    
    input("\nPresiona Enter para continuar...")

def buscar_cliente():
    """Función para buscar un cliente por ID"""
    print("\n🔍 BUSCAR CLIENTE POR ID")
    print("-" * 30)
    
    try:
        id_cliente = input("ID del cliente: ").strip()
        if not id_cliente:
            print("❌ Debes ingresar un ID")
            return
        
        cliente = ClienteDAO.buscar_por_id(int(id_cliente))
        if cliente:
            print(f"✅ Cliente encontrado: {cliente}")
    except ValueError:
        print("❌ El ID debe ser un número")
    except Exception as e:
        print(f"❌ Error al buscar: {e}")
    
    input("\nPresiona Enter para continuar...")

def actualizar_cliente():
    """Función para actualizar un cliente"""
    print("\n✏️  ACTUALIZAR CLIENTE")
    print("-" * 30)
    
    try:
        id_cliente = input("ID del cliente a actualizar: ").strip()
        if not id_cliente:
            print("❌ Debes ingresar un ID")
            return
        
        # Buscar el cliente existente
        cliente_existente = ClienteDAO.buscar_por_id(int(id_cliente))
        if not cliente_existente:
            return
        
        print(f"Cliente actual: {cliente_existente}")
        print("\nIngresa los nuevos datos (deja vacío para mantener el actual):")
        
        nombre = input(f"Nuevo nombre [{cliente_existente.nombre}]: ").strip()
        apellido = input(f"Nuevo apellido [{cliente_existente.apellido}]: ").strip()
        telefono = input(f"Nuevo teléfono [{cliente_existente.telefono}]: ").strip()
        email = input(f"Nuevo email [{cliente_existente.email}]: ").strip()
        
        # Usar valores existentes si no se ingresan nuevos
        nombre = nombre if nombre else cliente_existente.nombre
        apellido = apellido if apellido else cliente_existente.apellido
        telefono = telefono if telefono else cliente_existente.telefono
        email = email if email else cliente_existente.email
        
        cliente_actualizado = Cliente(
            id=int(id_cliente),
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            email=email
        )
        
        ClienteDAO.actualizar(cliente_actualizado)
        
    except ValueError:
        print("❌ El ID debe ser un número")
    except Exception as e:
        print(f"❌ Error al actualizar: {e}")
    
    input("\nPresiona Enter para continuar...")

def eliminar_cliente():
    """Función para eliminar un cliente"""
    print("\n🗑️  ELIMINAR CLIENTE")
    print("-" * 30)
    
    try:
        id_cliente = input("ID del cliente a eliminar: ").strip()
        if not id_cliente:
            print("❌ Debes ingresar un ID")
            return
        
        # Buscar el cliente antes de eliminar
        cliente = ClienteDAO.buscar_por_id(int(id_cliente))
        if not cliente:
            return
        
        print(f"Cliente a eliminar: {cliente}")
        confirmacion = input("¿Estás seguro? (s/N): ").strip().lower()
        
        if confirmacion in ['s', 'si', 'sí', 'y', 'yes']:
            ClienteDAO.eliminar(int(id_cliente))
        else:
            print("❌ Operación cancelada")
            
    except ValueError:
        print("❌ El ID debe ser un número")
    except Exception as e:
        print(f"❌ Error al eliminar: {e}")
    
    input("\nPresiona Enter para continuar...")

def main():
    """Función principal del programa"""
    while True:
        try:
            limpiar_pantalla()
            mostrar_menu()
            
            opcion = input("\nSelecciona una opción (1-6): ").strip()
            
            if opcion == "1":
                insertar_cliente()
            elif opcion == "2":
                listar_clientes()
            elif opcion == "3":
                buscar_cliente()
            elif opcion == "4":
                actualizar_cliente()
            elif opcion == "5":
                eliminar_cliente()
            elif opcion == "6":
                print("\n👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida. Selecciona 1-6")
                input("Presiona Enter para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrumpido por el usuario")
            break
        except Exception as e:
            print(f"\n❌ Error inesperado: {e}")
            input("Presiona Enter para continuar...")

if __name__ == "__main__":
    main()
