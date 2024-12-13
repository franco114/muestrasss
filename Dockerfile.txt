# Usa una imagen base oficial de Python 3.10
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt en el directorio de trabajo
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido del proyecto en el directorio de trabajo
COPY . .

# Realiza las migraciones de la base de datos
RUN python manage.py migrate

# Recoge los archivos estáticos
RUN python manage.py collectstatic --noinput

# Expone el puerto 8000
EXPOSE 8000

# Define el comando de inicio para ejecutar el servidor Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "tu_proyecto.wsgi:application"]
