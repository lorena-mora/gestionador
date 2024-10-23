Instrucciones para Ejecutar la API de Gestión de Tareas Localmente
Requisitos Previos

Instalar XAMPP:
Descarga e instala XAMPP.
Inicia el servicio de MySQL (MariaDB) desde el panel de control de XAMPP.

Instalar Python 3:
Asegúrate de tener instalada una versión de Python 3 en tu sistema. Puedes descargarlo desde python.org.

Verifica la instalación ejecutando:
python --version

Instalar Git (opcional para clonación de repositorio):

Instala Git desde git-scm.com.
Verifica la instalación ejecutando:

git --version

Paso 1: Clonar el Repositorio
Abre una terminal o línea de comandos y navega al directorio donde deseas clonar el proyecto.
Ejecuta el siguiente comando para clonar el repositorio:

git clone https://github.com/lorena-mora/gestionador.git

Ingresa al directorio del proyecto:
cd gestor_tareas

Paso 2: Crear y Activar un Entorno Virtual

Crea un entorno virtual:
python -m venv entorno_virtual

Activa el entorno virtual:
En Windows:
entorno_virtual\Scripts\activate

En macOS/Linux:
source entorno_virtual/bin/activate

Paso 3: Instalar Dependencias
Con el entorno virtual activado, instala todas las dependencias necesarias usando:

pip install -r requirements.txt

Paso 4: Configurar la Base de Datos en XAMPP
Iniciar el Servidor MySQL (MariaDB):
Abre XAMPP y asegúrate de que el servicio MySQL esté activo.
Crear la Base de Datos:
Abre phpMyAdmin en tu navegador (http://localhost/phpmyadmin).
Crea una nueva base de datos llamada tareas_control.
Dentro de esta base de datos, crea la tabla registro_tareas si es necesario:

CREATE TABLE registro_tareas (
    id_registro INT AUTO_INCREMENT PRIMARY KEY,
    titulo_tarea VARCHAR(255) NOT NULL,
    descripcion_tarea TEXT NOT NULL
);

Paso 5: Aplicar Migraciones de Django
Ejecuta las siguientes migraciones para preparar la base de datos:

python manage.py makemigrations
python manage.py migrate

Paso 6: Crear un Superusuario (Opcional para Administrar desde el Panel de Admin)
Crea un superusuario para acceder al panel de administración:

python manage.py createsuperuser

Paso 7: Ejecutar el Servidor de Desarrollo
Inicia el servidor de desarrollo de Django:
python manage.py runserver
Accede a la API desde tu navegador en http://127.0.0.1:8000/api/tareas/.

Paso 8: Uso de la API con Postman (Opcional)
Obtener Lista de Tareas (GET):

Endpoint: GET http://127.0.0.1:8000/api/tareas/
Agregar Nueva Tarea (POST):

Endpoint: POST http://127.0.0.1:8000/api/tareas/agregar/
JSON Body:
{
  "titulo_tarea": "Ejemplo de Tarea",
  "descripcion_tarea": "Descripción detallada de la tarea."
}

Actualizar Tarea Existente (PUT):
Endpoint: PUT http://127.0.0.1:8000/api/tareas/actualizar/<id>
JSON Body:
{
  "titulo_tarea": "Tarea Actualizada",
  "descripcion_tarea": "Nueva descripción de la tarea."
}
Eliminar Tarea (DELETE):
Endpoint: DELETE http://127.0.0.1:8000/api/tareas/eliminar/<id>
