# 🚀 Despliegue en Railway - Sistema de Gestión de Clientes

## 📋 Pasos para Desplegar en Railway

### 1. Preparar Base de Datos MySQL
1. En Railway, agrega un servicio **MySQL**
2. Copia las credenciales de conexión
3. Configura las variables de entorno

### 2. Variables de Entorno en Railway
Configura estas variables en tu proyecto Railway:

```
MYSQL_HOST=<tu_host_mysql_railway>
MYSQL_USER=<tu_usuario_mysql>
MYSQL_PASSWORD=<tu_password_mysql>
MYSQL_DATABASE=railway
MYSQL_PORT=3306
FLASK_ENV=production
```

### 3. Conectar Repositorio GitHub
1. En Railway, conecta tu repositorio: `https://github.com/barcebaro19/Trabajo_Python`
2. Railway detectará automáticamente los archivos de configuración

### 4. Importar Datos de Base de Datos
1. Conecta a tu MySQL local y exporta datos:
```sql
mysqldump -u root -p persona cliente > cliente_data.sql
```

2. Importa a Railway MySQL:
```sql
mysql -h <railway_host> -u <user> -p<password> railway < cliente_data.sql
```

### 5. Archivos de Configuración Creados
- ✅ `Procfile` - Comando de inicio
- ✅ `railway.json` - Configuración Railway
- ✅ `requirements.txt` - Dependencias Python
- ✅ `.env.example` - Variables de entorno ejemplo

## 🌐 URL de Acceso
Una vez desplegado, tu aplicación estará disponible en:
`https://tu-proyecto.railway.app`

## 🔧 Comandos Útiles

### Verificar logs en Railway:
```bash
railway logs
```

### Conectar a base de datos Railway:
```bash
railway connect mysql
```

## 📊 Funcionalidades Disponibles
- ✅ Gestión completa de clientes (CRUD)
- ✅ Interfaz Bootstrap responsiva
- ✅ Base de datos MySQL en la nube
- ✅ Escalabilidad automática
