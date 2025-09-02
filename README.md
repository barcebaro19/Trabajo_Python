# 🗃️ CRUD de Clientes en Python con MySQL

Sistema completo de gestión de clientes (Create, Read, Update, Delete) desarrollado en Python con conexión a base de datos MySQL.

## 📋 Características

- ✅ **Conexión segura** a MySQL con pool de conexiones
- ✅ **Operaciones CRUD completas**: Insertar, Listar, Buscar, Actualizar, Eliminar
- ✅ **Interfaz de línea de comandos** intuitiva y fácil de usar
- ✅ **Manejo de errores** robusto
- ✅ **Validación de datos** en todas las operaciones
- ✅ **Código limpio y bien estructurado**

## 🚀 Instalación

### 1. Requisitos Previos

- Python 3.7 o superior
- MySQL Server 5.7 o superior
- Acceso a MySQL con usuario `root` (sin contraseña por defecto)

### 2. Instalar Dependencias

```bash
pip install mysql-connector-python
```

### 3. Configurar Base de Datos

1. **Abrir MySQL Workbench** o línea de comandos de MySQL
2. **Ejecutar el script** `crear_tabla.sql` para crear la base de datos y tabla
3. **Verificar** que la base de datos `persona` y tabla `cliente` existan

### 4. Configurar Conexión

Si tu MySQL tiene contraseña o configuración diferente, edita `main.py`:

```python
dbconfig = {
    "host": "localhost",      # Cambia si MySQL está en otro servidor
    "user": "root",          # Cambia tu usuario de MySQL
    "passwd": "tu_password", # Cambia tu contraseña
    "database": "persona"    # Cambia el nombre de la BD si es necesario
}
```

## 🎯 Uso del Sistema

### 1. Probar Conexión

```bash
python test_conexion.py
```

Este comando verificará:
- ✅ Conexión a MySQL
- ✅ Existencia de la base de datos
- ✅ Existencia de la tabla cliente
- ✅ Operaciones básicas del CRUD

### 2. Ejecutar Menú Principal

```bash
python menu_crud.py
```

El menú te permitirá:
- 📝 **Insertar** nuevos clientes
- 📋 **Listar** todos los clientes
- 🔍 **Buscar** clientes por ID
- ✏️ **Actualizar** información de clientes
- 🗑️ **Eliminar** clientes

### 3. Usar Archivos Individuales

También puedes ejecutar operaciones específicas:

```bash
# Insertar cliente
python insertar.py

# Actualizar cliente
python actualizar.py

# Eliminar cliente
python eliminar.py
```

## 🗂️ Estructura del Proyecto

```
Apy_Python/
├── api_python/
│   ├── __init__.py
│   ├── app.py
│   ├── cliente.py          # Modelo de datos
│   ├── cliente_dao.py      # Operaciones de base de datos
│   └── conexion.py         # Conexión individual (no usado)
├── main.py                 # Pool de conexiones principal
├── menu_crud.py            # Menú interactivo principal
├── test_conexion.py        # Pruebas del sistema
├── insertar.py             # Insertar cliente
├── actualizar.py           # Actualizar cliente
├── eliminar.py             # Eliminar cliente
├── conector.py             # Prueba de conexión
├── crear_tabla.sql         # Script SQL para crear BD
└── README.md               # Este archivo
```

## 🔧 Solución de Problemas

### Error de Conexión

Si obtienes error de conexión:

1. **Verifica que MySQL esté ejecutándose**
2. **Comprueba las credenciales** en `main.py`
3. **Asegúrate de que la base de datos existe**
4. **Verifica que la tabla cliente esté creada**

### Error de Tabla

Si la tabla no existe:

1. **Ejecuta** `crear_tabla.sql` en MySQL
2. **Verifica** que la base de datos `persona` exista
3. **Comprueba** que tengas permisos de CREATE TABLE

### Error de Módulo

Si hay errores de importación:

1. **Verifica** que estés en el directorio correcto
2. **Asegúrate** de que todos los archivos estén presentes
3. **Comprueba** que Python esté en tu PATH

## 📊 Estructura de la Tabla Cliente

```sql
CREATE TABLE cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

## 🎉 Ejemplos de Uso

### Insertar Cliente
```python
from api_python.cliente_dao import ClienteDAO
from api_python.cliente import Cliente

nuevo = Cliente(
    nombre="Ana",
    apellido="García",
    telefono="555123456",
    email="ana.garcia@email.com"
)
ClienteDAO.insertar(nuevo)
```

### Listar Clientes
```python
from api_python.cliente_dao import ClienteDAO

clientes = ClienteDAO.listar()
for cliente in clientes:
    print(cliente)
```

### Actualizar Cliente
```python
from api_python.cliente_dao import ClienteDAO
from api_python.cliente import Cliente

cliente_editado = Cliente(
    id=1,
    nombre="Juan Carlos",
    apellido="Pérez",
    telefono="999888777",
    email="juan.carlos@email.com"
)
ClienteDAO.actualizar(cliente_editado)
```

## 🤝 Contribuir

Si encuentras errores o quieres mejorar el código:

1. **Reporta el problema** con detalles
2. **Sugiere mejoras** específicas
3. **Mantén el código limpio** y bien documentado

## 📝 Licencia

Este proyecto es de uso libre para fines educativos y comerciales.

---

**¡Disfruta usando tu CRUD de Clientes! 🎯**
