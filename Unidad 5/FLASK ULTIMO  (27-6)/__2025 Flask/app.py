from flask import Flask, render_template, request, redirect, flash
from datetime import datetime, date
from models import db
from models import RegistroHorario
from models import Trabajador

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route('/')
def inicio():
    return render_template('base.html')

@app.route('/registrar_entrada', methods=['GET', 'POST'])
def registrar_entrada():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni = request.form['dni']
        dependencia = request.form['dependencia']
        hoy = date.today()

        trabajador = Trabajador.query.filter_by(legajo=legajo, dni=dni).first()
        if not trabajador:
            flash('Trabajador no encontrado.')
            return redirect('/registrar_entrada')

        entrada_existente = RegistroHorario.query.filter_by(legajo=legajo, fecha=hoy).first()
        if entrada_existente:
            flash('Ya existe un registro de entrada para hoy.')
            return redirect('/registrar_entrada')

        nuevo_registro = RegistroHorario(
            legajo=legajo,
            fecha=hoy,
            hora_entrada=datetime.now().time(),
            dependencia=dependencia
        )
        db.session.add(nuevo_registro)
        db.session.commit()
        flash('Entrada registrada correctamente.')
        return redirect('/')
    
    return render_template('registrar_entrada.html')

@app.route('/registrar_salida', methods=['GET', 'POST'])
def registrar_salida():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni = request.form['dni']
        hoy = date.today()

        trabajador = Trabajador.query.filter_by(legajo=legajo, dni=dni).first()
        if not trabajador:
            flash('Trabajador no encontrado.')
            return redirect('/registrar_salida')

        registro = RegistroHorario.query.filter_by(legajo=legajo, fecha=hoy).first()
        if not registro or registro.hora_salida:
            flash('No hay entrada previa registrada o ya se registró la salida.')
            return redirect('/registrar_salida')

        registro.hora_salida = datetime.now().time()
        db.session.commit()
        flash('Salida registrada correctamente.')
        return redirect('/')
    
    return render_template('registrar_salida.html')

@app.route('/consultar', methods=['GET', 'POST'])
def consultar_registros():
    registros = []
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni = request.form['dni']
        desde = request.form['desde']
        hasta = request.form['hasta']

        trabajador = Trabajador.query.filter_by(legajo=legajo, dni=dni).first()
        if not trabajador:
            flash('Trabajador no encontrado.')
            return redirect('/consultar')

        registros = RegistroHorario.query.filter(
            RegistroHorario.legajo == legajo,
            RegistroHorario.fecha >= desde,
            RegistroHorario.fecha <= hasta
        ).order_by(RegistroHorario.fecha.asc()).all()
    
    return render_template('consultar_registros.html', registros=registros)

# A implementar: generación de reportes para administrativos

if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()  # Esto crea todas las tablas
    
# Es fundamental la creación de la base de datos, con la instrucción db.create_all(), teniendo en cuenta que solo la creará si ésta no existe.
    