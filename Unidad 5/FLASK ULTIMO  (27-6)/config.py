import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# ARCHIVO - config.py
# Para sqlite3 solo es necesario establecer la URI de la base de datos:
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'datos.sqlite3')}"
# Indica el nombre del archivo que CONTIENE la BASE DE DATOS. En este caso es una base de datos que corresponde al ADMINISTRADOR sqlite y se llama "datos.sqlite3".
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Si se establece en True, Flask-SQLAlchemy rastreará las MODIFICACIONES de los objetos y emitirá señales. Esto requiere MEMORIA ADICIONAL y debe DESHABILITARSE si no es necesario.          

SECRET_KEY = "OLAPUTOS" 
# Clave secreta que se usará en ciertas operaciones que requieren SEGURIDAD, por ejemplo cuando se crea una SESIÓN.

