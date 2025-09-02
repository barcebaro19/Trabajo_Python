# -*- coding: utf-8 -*-
from api_python.cliente_dao import ClienteDAO
from api_python.cliente import Cliente
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n" + "="*50)
    print("SISTEMA CRUD - GESTION DE CLIENTES")
    print("="*50)
    print("1. Listar todos los clientes")
    print("2. Insertar nuevo cliente")
    print("3. Actualizar cliente existente")
    print("4. Eliminar cliente")
    print("5. Probar conexion a BD")
    print("6. Salir")
    print("="*50)

def listar_clientes():
    print("\nLISTADO DE CLIENTES:")
    print("-" * 40)
    clientes = ClienteDAO.listar()
    if clientes:
        for cliente in clientes:
            print(f"ID: {cliente.id} | {cliente.nombre} {cliente.apellido} | Tel: {cliente.telefono}")
    else:
        print("No hay clientes registrados")
    input("\nPresiona Enter para continuar...")

def insertar_cliente():
    print("\nINSERTAR NUEVO CLIENTE:")
    print("-" * 30)
    try:
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        telefono = input("Telefono: ").strip()
        
        if not nombre or not apellido or not telefono:
            print("Todos los campos son obligatorios")
            return
            
        nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono)
        ClienteDAO.insertar(nuevo_cliente)
        
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPresiona Enter para continuar...")

def actualizar_cliente():
    print("\nACTUALIZAR CLIENTE:")
    print("-" * 25)
    
    # Mostrar clientes existentes
    clientes = ClienteDAO.listar()
    if not clientes:
        print("No hay clientes para actualizar")
        input("\nPresiona Enter para continuar...")
        return
    
    print("Clientes disponibles:")
    for cliente in clientes:
        print(f"ID: {cliente.id} - {cliente.nombre} {cliente.apellido}")
    
    try:
        id_cliente = int(input("\nIngresa el ID del cliente a actualizar: "))
        nombre = input("Nuevo nombre: ").strip()
        apellido = input("Nuevo apellido: ").strip()
        telefono = input("Nuevo telefono: ").strip()
        
        if not nombre or not apellido or not telefono:
            print("Todos los campos son obligatorios")
            return
            
        cliente_actualizado = Cliente(id=id_cliente, nombre=nombre, apellido=apellido, telefono=telefono)
        ClienteDAO.actualizar(cliente_actualizado)
        
    except ValueError:
        print("ID debe ser un numero")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPresiona Enter para continuar...")

def eliminar_cliente():
    print("\nELIMINAR CLIENTE:")
    print("-" * 20)
    
    # Mostrar clientes existentes
    clientes = ClienteDAO.listar()
    if not clientes:
        print("No hay clientes para eliminar")
        input("\nPresiona Enter para continuar...")
        return
    
    print("Clientes disponibles:")
    for cliente in clientes:
        print(f"ID: {cliente.id} - {cliente.nombre} {cliente.apellido}")
    
    try:
        id_cliente = int(input("\nIngresa el ID del cliente a eliminar: "))
        confirmacion = input(f"Estas seguro de eliminar el cliente con ID {id_cliente}? (s/n): ")
        
        if confirmacion.lower() == 's':
            ClienteDAO.eliminar(id_cliente)
        else:
            print("Operacion cancelada")
            
    except ValueError:
        print("ID debe ser un numero")
    except Exception as e:
        print(f"Error: {e}")
    
    input("\nPresiona Enter para continuar...")

def probar_conexion():
    print("\nPROBANDO CONEXION A BASE DE DATOS:")
    print("-" * 40)
    try:
        from main import get_connection
        conexion = get_connection()
        if conexion and conexion.is_connected():
            print("Conexion exitosa a MySQL")
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM cliente")
            total = cursor.fetchone()[0]
            print(f"Total de clientes en BD: {total}")
            cursor.close()
            conexion.close()
        else:
            print("No se pudo conectar a la base de datos")
    except Exception as e:
        print(f"Error de conexion: {e}")
    
    input("\nPresiona Enter para continuar...")

def main():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        try:
            opcion = input("\nSelecciona una opcion (1-6): ").strip()
            
            if opcion == "1":
                listar_clientes()
            elif opcion == "2":
                insertar_cliente()
            elif opcion == "3":
                actualizar_cliente()
            elif opcion == "4":
                eliminar_cliente()
            elif opcion == "5":
                probar_conexion()
            elif opcion == "6":
                print("\nHasta luego!")
                break
            else:
                print("Opcion invalida. Selecciona del 1 al 6.")
                input("\nPresiona Enter para continuar...")
                
        except KeyboardInterrupt:
            print("\n\nHasta luego!")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
