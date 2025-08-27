from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Trabajador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    legajo = db.Column(db.String(10), unique=True, nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    horas_semanales = db.Column(db.Integer, nullable=False)
    funcion = db.Column(db.String(2), nullable=False)  # DO, AD, TE

class RegistroHorario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    legajo = db.Column(db.String(10), db.ForeignKey('trabajador.legajo'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora_entrada = db.Column(db.Time, nullable=True)
    hora_salida = db.Column(db.Time, nullable=True)
    dependencia = db.Column(db.String(3), nullable=False)  # D01, D02, D03
