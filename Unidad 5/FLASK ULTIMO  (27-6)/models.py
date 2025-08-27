from __main__ import app
from flask_sqlalchemy import SQLAlchemy
import random

db = SQLAlchemy(app)

class Sucursal(db.Model):
    id = db.Column(db.Integer, primary_key=True)                      # El atributo id se establece como clave primaria de la tabla, ésta es administrada automáticamente por Flask-SQLAlchemy.
    
    numero = db.Column(db.String(50), unique=True, nullable=False)
    provincia = db.Column(db.String(100), nullable=False)
    localidad = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    repartidores = db.relationship('Repartidor', backref='sucursal', lazy=True)
    paquetes = db.relationship('Paquete', backref='sucursal', lazy=True)
    transportes = db.relationship('Transporte', backref='sucursal', lazy=True)

# Para que la relación sea BIDIRECCIONAL, usar el parámetro "backref" del método "relationship()".

# Cuando se define una clase que HEREDA de db.Model (CLASE BASE), se está definiendo un MODELO de base de datos DEFINIDO POR EL USUARIO para el MAPEO. Esto significa que cada instancia de esa clase representará una FILA en una TABLA de la base de datos, y cada ATRIBUTO de la clase representará una COLUMNA en esa tabla.


class Repartidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    paquetes = db.relationship('Paquete', backref='repartidor', lazy=True)
    numero = db.Column(db.String(50), unique=True, nullable=False)

class Paquete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numeroenvio = db.Column(db.String(4), default=lambda: '1{:03d}'.format(random.randint(0, 999), unique=True, nullable=False))
    peso = db.Column(db.Float, nullable=False)
    nomdestinatario = db.Column(db.String(100), nullable=False)
    dirdestinatario = db.Column(db.String(200), nullable=False)
    entregado = db.Column(db.Boolean, default=False)
    observaciones = db.Column(db.Text, default="", nullable=True)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=True)
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'), default=None) # 25/6 añadí "default=None"
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'), default=None) # 25/6 añadí "default=None"

class Transporte(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numerotransporte = db.Column(db.String(3), default=lambda: '2{:02d}'.format(random.randint(0, 99), unique=True, nullable=False))
    fechahorasalida = db.Column(db.DateTime, nullable=False)
    fechahorallegada = db.Column(db.DateTime, nullable=True)  # Permitir valores nulos
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'), nullable=False)
    paquetes = db.relationship('Paquete', backref='transporte', lazy=True)
