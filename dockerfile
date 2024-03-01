# Utiliza la imagen oficial de Python como base
FROM python:3.11.2

# Establece el directorio de trabajo en /app dentro del contenedor
WORKDIR /app

# Copia todo el contenido del directorio actual al directorio de trabajo /app dentro del contenedor
COPY . /app

# Instala las dependencias de tu aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 8080 (puerto interno de la aplicación FastAPI)
EXPOSE 8080

# Comando para ejecutar la aplicación FastAPI cuando se inicie el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
