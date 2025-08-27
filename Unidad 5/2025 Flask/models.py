from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trabajador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    legajo = db.Column(db.Integer, unique=True, nullable=False)
    dni = db.Column(db.String(8), nullable=False)
    nombre = db.Column(db.String(50), nullable=False)
    apellido = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    horas = db.Column(db.Integer, nullable=False)
    funcion = db.Column(db.String(2), nullable=False)  # DO - Docente, AD - Administrativo, TE - Técnico.

class RegistroHorario(db.Model):
    __tablename__ = 'registrohorario'  # Nombre exacto de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)
    idtrabajador = db.Column(db.Integer, db.ForeignKey('trabajador.id'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    horaentrada = db.Column(db.Time, nullable=True)
    horasalida = db.Column(db.Time, nullable=True)
    dependencia = db.Column(db.String(3), nullable=False)  # D01 - Edificio Central, D02 - Talleres, D03 - Centro Deportivo.
