from api_python.cliente_dao import ClienteDAO
from api_python.cliente import Cliente
import os


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    print("\n" + "="*50)
    print("🏢 SISTEMA CRUD - GESTIÓN DE CLIENTES")
    print("="*50)
    print("1. 📋 Listar todos los clientes")
    print("2. ➕ Insertar nuevo cliente")
    print("3. ✏️  Actualizar cliente existente")
    print("4. 🗑️  Eliminar cliente")
    print("5. 🔍 Probar conexión a BD")
    print("6. 🚪 Salir")
    print("="*50)

def listar_clientes():
    print("\n📋 LISTADO DE CLIENTES:")
    print("-" * 40)
    clientes = ClienteDAO.listar()
    if clientes:
        for cliente in clientes:
            print(f"ID: {cliente.id} | {cliente.nombre} {cliente.apellido} | Tel: {cliente.telefono}")
    else:
        print("❌ No hay clientes registrados")
    input("\nPresiona Enter para continuar...")

def insertar_cliente():
    print("\n➕ INSERTAR NUEVO CLIENTE:")
    print("-" * 30)
    try:
        nombre = input("Nombre: ").strip()
        apellido = input("Apellido: ").strip()
        telefono = input("Teléfono: ").strip()
        
        if not nombre or not apellido or not telefono:
            print("❌ Todos los campos son obligatorios")
            return
            
        nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono)
        ClienteDAO.insertar(nuevo_cliente)
        
    except Exception as e:
        print(f"❌ Error: {e}")
    
    input("\nPresiona Enter para continuar...")

def actualizar_cliente():
    print("\n✏️ ACTUALIZAR CLIENTE:")
    print("-" * 25)
    
    # Mostrar clientes existentes
    clientes = ClienteDAO.listar()
    if not clientes:
        print("❌ No hay clientes para actualizar")
        input("\nPresiona Enter para continuar...")
        return
    
    print("Clientes disponibles:")
    for cliente in clientes:
        print(f"ID: {cliente.id} - {cliente.nombre} {cliente.apellido}")
    
    try:
        id_cliente = int(input("\nIngresa el ID del cliente a actualizar: "))
        nombre = input("Nuevo nombre: ").strip()
        apellido = input("Nuevo apellido: ").strip()
        telefono = input("Nuevo teléfono: ").strip()
        
        if not nombre or not apellido or not telefono:
            print("❌ Todos los campos son obligatorios")
            return
            
        cliente_actualizado = Cliente(id=id_cliente, nombre=nombre, apellido=apellido, telefono=telefono)
        ClienteDAO.actualizar(cliente_actualizado)
        
    except ValueError:
        print("❌ ID debe ser un número")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    input("\nPresiona Enter para continuar...")

def eliminar_cliente():
    print("\n🗑️ ELIMINAR CLIENTE:")
    print("-" * 20)
    
    # Mostrar clientes existentes
    clientes = ClienteDAO.listar()
    if not clientes:
        print("❌ No hay clientes para eliminar")
        input("\nPresiona Enter para continuar...")
        return
    
    print("Clientes disponibles:")
    for cliente in clientes:
        print(f"ID: {cliente.id} - {cliente.nombre} {cliente.apellido}")
    
    try:
        id_cliente = int(input("\nIngresa el ID del cliente a eliminar: "))
        confirmacion = input(f"¿Estás seguro de eliminar el cliente con ID {id_cliente}? (s/n): ")
        
        if confirmacion.lower() == 's':
            ClienteDAO.eliminar(id_cliente)
        else:
            print("❌ Operación cancelada")
            
    except ValueError:
        print("❌ ID debe ser un número")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    input("\nPresiona Enter para continuar...")

def probar_conexion():
    print("\n🔍 PROBANDO CONEXIÓN A BASE DE DATOS:")
    print("-" * 40)
    try:
        from main import get_connection
        conexion = get_connection()
        if conexion and conexion.is_connected():
            print("✅ Conexión exitosa a MySQL")
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM cliente")
            total = cursor.fetchone()[0]
            print(f"📊 Total de clientes en BD: {total}")
            cursor.close()
            conexion.close()
        else:
            print("❌ No se pudo conectar a la base de datos")
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
    
    input("\nPresiona Enter para continuar...")

def main():
    while True:
        limpiar_pantalla()
        mostrar_menu()
        
        try:
            opcion = input("\n🔸 Selecciona una opción (1-6): ").strip()
            
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
                print("\n👋 ¡Hasta luego!")
                break
            else:
                print("❌ Opción inválida. Selecciona del 1 al 6.")
                input("\nPresiona Enter para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()
