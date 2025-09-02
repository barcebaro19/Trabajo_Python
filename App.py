from flask import Flask, render_template, request, redirect, url_for, flash
from api_python.cliente_dao import ClienteDAO
from api_python.cliente import Cliente

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

@app.route('/')
@app.route('/index.html')
def inicio():
    """Página principal que muestra la tabla de clientes"""
    try:
        clientes = ClienteDAO.listar()
        print(f"Clientes obtenidos: {len(clientes)}")  # Debug
        for cliente in clientes:
            print(f"Cliente: {cliente}")  # Debug
        return render_template('index.html', clientes=clientes)
    except Exception as e:
        print(f"Error en inicio(): {e}")  # Debug
        flash(f'Error al cargar clientes: {str(e)}', 'error')
        return render_template('index.html', clientes=[])

@app.route('/insertar', methods=['POST'])
def insertar_cliente():
    """Insertar nuevo cliente"""
    try:
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        telefono = request.form.get('telefono')
        email = request.form.get('email')
        
        if nombre and apellido:
            nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, email=email)
            ClienteDAO.insertar(nuevo_cliente)
            flash('Cliente insertado correctamente', 'success')
        else:
            flash('Nombre y apellido son requeridos', 'error')
    except Exception as e:
        flash(f'Error al insertar cliente: {str(e)}', 'error')
    
    return redirect(url_for('inicio'))

@app.route('/actualizar', methods=['POST'])
def actualizar_cliente():
    """Actualizar cliente existente"""
    try:
        id_cliente = request.form.get('id')
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        telefono = request.form.get('telefono')
        email = request.form.get('email')
        
        if id_cliente and nombre and apellido:
            cliente_editado = Cliente(id=int(id_cliente), nombre=nombre, apellido=apellido, telefono=telefono, email=email)
            ClienteDAO.actualizar(cliente_editado)
            flash('Cliente actualizado correctamente', 'success')
        else:
            flash('ID, nombre y apellido son requeridos', 'error')
    except Exception as e:
        flash(f'Error al actualizar cliente: {str(e)}', 'error')
    
    return redirect(url_for('inicio'))

@app.route('/eliminar/<int:id_cliente>')
def eliminar_cliente(id_cliente):
    """Eliminar cliente por ID"""
    try:
        ClienteDAO.eliminar(id_cliente)
        flash('Cliente eliminado correctamente', 'success')
    except Exception as e:
        flash(f'Error al eliminar cliente: {str(e)}', 'error')
    
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    import os
    # Para Railway (producción) o local (desarrollo)
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)
