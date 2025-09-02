#!/usr/bin/env python3
"""
Script para ejecutar la aplicación Flask desde PyCharm
Ejecuta este archivo en lugar del index.html para que funcione correctamente
"""

from app import app

if __name__ == '__main__':
    print("🚀 Iniciando aplicación Flask...")
    print("📍 Accede desde tu navegador en: http://127.0.0.1:5000")
    print("🔧 Para detener la aplicación presiona Ctrl+C")
    app.run(host='127.0.0.1', port=5000, debug=True)
