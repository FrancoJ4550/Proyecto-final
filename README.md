# Proyecto final Museos de la UNAM

Este proyecto es una aplicación web que implementa Flask, html, css, javascript y sqlite para mostrar información general sobre los museos que se pueden visitar en la zona de Ciudad Universitaria. La aplicación permite navegar por varias páginas.  En la página principal se navega con los ovalos en la parte inferior de la pantalla, las otras páginas tienen una barra de navegación. Además, al final de cada página hay una sección de comentarios en donde se puede dejar, eliminar y editar comentarios. La aplicación web usa sqlite para gestionar los comentarios en esta sección. (El ID del comentario es el número antes del nombre de usuario).

## Configuración

Para comenzar, sigue estos pasos:

### 1. Clonar el Repositorio

Clona este repositorio a tu máquina local usando:

```bash
git clone URL_DEL_REPOSITORIO
```

### 2. Crear un Entorno Virtual

Es recomendable usar un entorno virtual para instalar las dependencias. Puedes crear uno usando:

```bash
python -m venv .venv
```

Activar el entorno virtual:

En Windows:
```bash
.venv\Scripts\activate
```

En MacOS/Linux:
```bash
source .venv/bin/activate
```

### 3. Instalar Dependencias

Instala las dependencias necesarias con:

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la Aplicación

Para ejecutar la aplicación, usa:

```bash
python app.py
```