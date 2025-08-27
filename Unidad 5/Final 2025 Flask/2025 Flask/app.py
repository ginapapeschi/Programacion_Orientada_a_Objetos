from flask import Flask, render_template, request, redirect, flash
from datetime import datetime, date
from models import db
from models import RegistroHorario
from models import Trabajador

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

@app.route('/')
def inicio():
    return render_template('base.html')

@app.route('/registrar_entrada', methods=['GET', 'POST'])
def registrar_entrada():
    if request.method == 'POST':
        leg = request.form['legajo']
        ultimos_dni = request.form['dni']
        dep = request.form['dependencia']
        hoy = date.today()

        if not ultimos_dni.isdigit() or len(ultimos_dni) != 4:
            flash('El DNI debe contener exactamente 4 dígitos numéricos.', 'danger')
            return redirect('/registrar_entrada')

        trabajador = Trabajador.query.filter_by(legajo=leg).first()
        if not trabajador:
            flash('Trabajador no encontrado.', 'danger')
            return redirect('/registrar_entrada')

        if not trabajador.dni.endswith(ultimos_dni):
            flash('Los últimos 4 dígitos del DNI no coinciden.', 'danger')
            return redirect('/registrar_entrada')

        existe_entrada = RegistroHorario.query.filter_by(idtrabajador=trabajador.id, fecha=hoy).first()
        if existe_entrada:
            flash('Ya existe un registro de entrada para hoy.', 'warning')
            return redirect('/registrar_entrada')

        nuevo_registro = RegistroHorario(idtrabajador=trabajador.id, fecha=hoy, horaentrada=datetime.now().time(), dependencia=dep)

        db.session.add(nuevo_registro)
        db.session.commit()
        flash('Entrada registrada correctamente.', 'success')
        return redirect('/registrar_entrada')
    
    return render_template('registrar_entrada.html')


@app.route('/registrar_salida', methods=['GET', 'POST'])
def registrar_salida():
    if request.method == 'POST':
        leg = request.form['legajo']
        ultimos_dni = request.form['dni']
        hoy = date.today()

        trabajador = Trabajador.query.filter_by(legajo=leg).first()
        if not trabajador:
            return render_template('registrar_salida.html', error='Trabajador no encontrado.')

        if not trabajador.dni.endswith(ultimos_dni):
            return render_template('registrar_salida.html', error='Los últimos 4 dígitos del DNI no coinciden.')

        registro = RegistroHorario.query.filter_by(idtrabajador=trabajador.id, fecha=hoy).first()
        
        if not registro:
            return render_template('registrar_salida.html', error='No hay entrada previa registrada para hoy.')

        if registro.horasalida:
            return render_template('registrar_salida.html', error='Ya se registró la salida.')

        if 'confirmar' in request.form:
            registro.horasalida = datetime.now().time()
            db.session.commit()
            flash('Salida registrada correctamente.', 'success')
            return redirect('/registrar_salida')
        else:
            return render_template('registrar_salida.html', legajo=leg, dni=ultimos_dni, dependencia=registro.dependencia, confirmar=True)

    return render_template('registrar_salida.html')


@app.route('/consultar', methods=['GET', 'POST'])
def consultar_registros():
    error = None
    registros = []
    mensaje_no_registros = None
    if request.method == 'POST':
        leg = request.form['legajo']
        ultimos_dni = request.form['ultimos_dni']
        desde = request.form['desde']
        hasta = request.form['hasta']

        if len(ultimos_dni) != 4 or not ultimos_dni.isdigit():
            error = 'Ingrese los últimos 4 dígitos del DNI correctamente.'
            return render_template('consultar_registros.html', error=error, registros=registros)

        trabajador = Trabajador.query.filter_by(legajo=leg).first()

        if not trabajador or not trabajador.dni.endswith(ultimos_dni):
            error = 'Trabajador no encontrado o DNI incorrecto.'
            return render_template('consultar_registros.html', error=error, registros=registros)

        try:
            fecha_desde = datetime.strptime(desde, '%Y-%m-%d').date()
            fecha_hasta = datetime.strptime(hasta, '%Y-%m-%d').date()
        except ValueError:
            error = 'Formato de fecha inválido.'
            return render_template('consultar_registros.html', error=error, registros=registros)

        if fecha_desde > fecha_hasta:
            error = 'La fecha "desde" no puede ser mayor que "hasta".'
            return render_template('consultar_registros.html', error=error, registros=registros)

        registros = RegistroHorario.query.filter(RegistroHorario.idtrabajador == trabajador.id, RegistroHorario.fecha >= fecha_desde, RegistroHorario.fecha <= fecha_hasta).order_by(RegistroHorario.fecha.asc()).all()

        if not registros:
            mensaje_no_registros = 'No se encontraron registros para ese rango de fechas.'

    return render_template('consultar_registros.html', error=error, registros=registros, mensaje_no_registros=mensaje_no_registros)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
