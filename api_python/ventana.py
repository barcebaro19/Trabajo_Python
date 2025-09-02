import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
from api_python.cliente_dao import ClienteDAO
from api_python.cliente import Cliente


class AppCRUD:
    def __init__(self, root):
        self.root = root
        self.root.title("🏢 Sistema CRUD - Gestión de Clientes")
        self.root.geometry("800x500")
        self.root.config(bg="#f0f4f7")

        # Frame lateral (menú)
        menu_frame = tk.Frame(root, bg="#2c3e50", width=200)
        menu_frame.pack(side="left", fill="y")

        # Botones del menú
        botones = [
            ("📋 Listar Clientes", self.listar_clientes),
            ("➕ Insertar Cliente", self.insertar_cliente),
            ("✏️ Actualizar Cliente", self.actualizar_cliente),
            ("🗑️ Eliminar Cliente", self.eliminar_cliente),
            ("🔍 Probar Conexión", self.probar_conexion),
            ("🚪 Salir", root.quit)
        ]

        for texto, comando in botones:
            btn = tk.Button(menu_frame, text=texto, command=comando,
                            bg="#34495e", fg="white", relief="flat", font=("Arial", 11), pady=10)
            btn.pack(fill="x", padx=10, pady=5)

        # Área de salida (ventana para ver cambios)
        self.text_area = tk.Text(root, wrap="word", bg="white", fg="black",
                                 font=("Consolas", 11))
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)

    def mostrar_mensaje(self, mensaje):
        """Muestra texto en la ventana de salida"""
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, mensaje)

    def listar_clientes(self):
        clientes = ClienteDAO.listar()
        if clientes:
            resultado = "📋 LISTADO DE CLIENTES\n" + "-" * 40 + "\n"
            for c in clientes:
                resultado += f"ID: {c.id} | {c.nombre} {c.apellido} | Tel: {c.telefono}\n"
        else:
            resultado = "❌ No hay clientes registrados"
        self.mostrar_mensaje(resultado)

    def insertar_cliente(self):
        nombre = simpledialog.askstring("Insertar Cliente", "Nombre:")
        apellido = simpledialog.askstring("Insertar Cliente", "Apellido:")
        telefono = simpledialog.askstring("Insertar Cliente", "Teléfono:")

        if not nombre or not apellido or not telefono:
            messagebox.showerror("Error", "❌ Todos los campos son obligatorios")
            return

        nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono)
        try:
            ClienteDAO.insertar(nuevo_cliente)
            messagebox.showinfo("Éxito", "✅ Cliente insertado correctamente")
            self.listar_clientes()
        except Exception as e:
            messagebox.showerror("Error", f"❌ {e}")

    def actualizar_cliente(self):
        clientes = ClienteDAO.listar()
        if not clientes:
            messagebox.showwarning("Atención", "❌ No hay clientes para actualizar")
            return

        ids = [str(c.id) for c in clientes]
        id_cliente = simpledialog.askstring("Actualizar Cliente", f"IDs disponibles: {', '.join(ids)}\n\nIngrese ID:")
        if not id_cliente or not id_cliente.isdigit():
            messagebox.showerror("Error", "❌ ID inválido")
            return

        nombre = simpledialog.askstring("Actualizar Cliente", "Nuevo nombre:")
        apellido = simpledialog.askstring("Actualizar Cliente", "Nuevo apellido:")
        telefono = simpledialog.askstring("Actualizar Cliente", "Nuevo teléfono:")

        if not nombre or not apellido or not telefono:
            messagebox.showerror("Error", "❌ Todos los campos son obligatorios")
            return

        cliente_actualizado = Cliente(id=int(id_cliente), nombre=nombre, apellido=apellido, telefono=telefono)
        try:
            ClienteDAO.actualizar(cliente_actualizado)
            messagebox.showinfo("Éxito", "✅ Cliente actualizado correctamente")
            self.listar_clientes()
        except Exception as e:
            messagebox.showerror("Error", f"❌ {e}")

    def eliminar_cliente(self):
        clientes = ClienteDAO.listar()
        if not clientes:
            messagebox.showwarning("Atención", "❌ No hay clientes para eliminar")
            return

        ids = [str(c.id) for c in clientes]
        id_cliente = simpledialog.askstring("Eliminar Cliente", f"IDs disponibles: {', '.join(ids)}\n\nIngrese ID:")
        if not id_cliente or not id_cliente.isdigit():
            messagebox.showerror("Error", "❌ ID inválido")
            return

        confirm = messagebox.askyesno("Confirmación", f"¿Seguro de eliminar cliente con ID {id_cliente}?")
        if confirm:
            try:
                ClienteDAO.eliminar(int(id_cliente))
                messagebox.showinfo("Éxito", "✅ Cliente eliminado correctamente")
                self.listar_clientes()
            except Exception as e:
                messagebox.showerror("Error", f"❌ {e}")

    def probar_conexion(self):
        try:
            from main import get_connection
            conexion = get_connection()
            if conexion and conexion.is_connected():
                cursor = conexion.cursor()
                cursor.execute("SELECT COUNT(*) FROM cliente")
                total = cursor.fetchone()[0]
                cursor.close()
                conexion.close()
                self.mostrar_mensaje(f"✅ Conexión exitosa\n📊 Total clientes en BD: {total}")
            else:
                self.mostrar_mensaje("❌ No se pudo conectar a la base de datos")
        except Exception as e:
            self.mostrar_mensaje(f"❌ Error de conexión: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = AppCRUD(root)
    root.mainloop()
