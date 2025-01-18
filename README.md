# Backend Evaluación TCIT Junior Python Dev

## Requisitos:

1. **Python** (versión 3.9 o superior).
2. **PostgreSQL** como base de datos.
3. **Pip** para gestionar paquetes de Python.
4. **Flask** y las dependencias del proyecto.
5. Archivo de configuración `.env` para las credenciales de la base de datos.

---

## Instrucciones de Configuración:

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/Jazmin-Contreras/post_backend.git
   cd post_backend
   ```

2. **Crear un entorno virtual**:
   ```bash
   python -m venv venv
   En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias**
   

4. **Configurar la base de datos**:
   - Con PostgreSQL en funcionamiento.
   - Crea una base de datos con el nombre `prueba_tcit` y crea la tabla "post"
   ```bash
   CREATE TABLE post (
	nombre VARCHAR(200) PRIMARY KEY,
	descripcion TEXT NOT NULL);
   ```
   - Configura un archivo `.env` en la raíz del proyecto con las siguientes variables:
     ```env
     SECRET_KEY=93637442*
     PGSQL_HOST=localhost
     PGSQL_USER=postgres
     PGSQL_PASSWORD=93637442
     PGSQL_DATABASE=prueba_tcit
     ```

5. **Inicializar la base de datos**


## Inicializar la API:

1. **Ejecutar la aplicación**:
   ```bash
   venv\Scripts\Activate
   python .\src\app.py
   ```

## Herramientas Utilizadas:

- **Lenguaje**: Python 3.9+
- **Framework**: Flask
- **Base de Datos**: PostgreSQL
- **Gestor de Dependencias**: Pip
- **CORS**: Flask-CORS
