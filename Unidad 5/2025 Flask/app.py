from flask import Flask, render_template, request, redirect, flash
from datetime import datetime, date, time
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
        legajo = request.form['legajo']
        ultimos_digitos_dni = request.form['dni']
        dependencia = request.form['dependencia']
        hoy = date.today()

        # Validar que el DNI tenga exactamente 4 dígitos numéricos
        if not ultimos_digitos_dni.isdigit() or len(ultimos_digitos_dni) != 4:
            flash('El DNI debe contener exactamente 4 dígitos numéricos.', 'danger')
            return redirect('/registrar_entrada')

        trabajador = Trabajador.query.filter_by(legajo=legajo).first()
        if not trabajador:
            flash('Legajo no encontrado.', 'danger')
            return redirect('/registrar_entrada')

        if not trabajador.dni.endswith(ultimos_digitos_dni):
            flash('Los últimos 4 dígitos del DNI no coinciden.', 'danger')
            return redirect('/registrar_entrada')

        entrada_existente = RegistroHorario.query.filter_by(idtrabajador=trabajador.id, fecha=hoy).first()
        if entrada_existente:
            flash('Ya existe un registro de entrada para hoy.', 'warning')
            return redirect('/registrar_entrada')

        nuevo_registro = RegistroHorario(
            idtrabajador=trabajador.id,
            fecha=hoy,
            horaentrada=datetime.now().time(),
            dependencia=dependencia
        )
        db.session.add(nuevo_registro)
        db.session.commit()
        flash('Entrada registrada correctamente.', 'success')
        return redirect('/registrar_entrada')
    
    return render_template('registrar_entrada.html')


@app.route('/registrar_salida', methods=['GET', 'POST'])
def registrar_salida():
    if request.method == 'POST':
        legajo = request.form['legajo']
        dni_ultimos4 = request.form['dni']
        hoy = date.today()

        trabajador = Trabajador.query.filter_by(legajo=legajo).first()
        if not trabajador:
            return render_template('registrar_salida.html', error='Trabajador no encontrado.')

        if not trabajador.dni.endswith(dni_ultimos4):
            return render_template('registrar_salida.html', error='Los últimos 4 dígitos del DNI no coinciden.')

        registro = RegistroHorario.query.filter_by(idtrabajador=trabajador.id, fecha=hoy).first()
        if not registro:
            return render_template('registrar_salida.html', error='No hay entrada previa registrada para hoy.')

        if registro.horasalida:
            return render_template('registrar_salida.html', error='Ya se registró la salida.')

        # Paso de confirmación
        if 'confirmar' in request.form:
            registro.horasalida = datetime.now().time()
            db.session.commit()
            flash('Salida registrada correctamente.', 'success')
            return redirect('/registrar_salida')
        else:
            # Mostrar confirmación antes de registrar
            return render_template('registrar_salida.html', 
                                   legajo=legajo, 
                                   dni=dni_ultimos4,
                                   dependencia=registro.dependencia,
                                   confirmar=True)

    return render_template('registrar_salida.html')



@app.route('/consultar', methods=['GET', 'POST'])
def consultar_registros():
    error = None
    registros = []
    mensaje_no_registros = None
    if request.method == 'POST':
        legajo = request.form['legajo']
        ultimos_dni = request.form['ultimos_dni']

        desde = request.form['desde']
        hasta = request.form['hasta']

        if len(ultimos_dni) != 4 or not ultimos_dni.isdigit():
            error = 'Ingrese los últimos 4 dígitos del DNI correctamente.'
            return render_template('consultar_registros.html', error=error, registros=registros)

        trabajador = Trabajador.query.filter(
            Trabajador.legajo == legajo,
            Trabajador.dni.like(f"%{ultimos_dni}")
        ).first()

        if not trabajador:
            error = 'Trabajador no encontrado.'
            return render_template('consultar_registros.html', error=error, registros=registros)

        try:
            desde_date = datetime.strptime(desde, '%Y-%m-%d').date()
            hasta_date = datetime.strptime(hasta, '%Y-%m-%d').date()
        except ValueError:
            error = 'Formato de fecha inválido.'
            return render_template('consultar_registros.html', error=error, registros=registros)

        if desde_date > hasta_date:
            error = 'La fecha "Desde" no puede ser mayor que "Hasta".'
            return render_template('consultar_registros.html', error=error, registros=registros)

        registros = RegistroHorario.query.filter(
            RegistroHorario.idtrabajador == trabajador.id,
            RegistroHorario.fecha >= desde_date,
            RegistroHorario.fecha <= hasta_date
        ).order_by(RegistroHorario.fecha.asc()).all()

        if not registros:
            mensaje_no_registros = 'No se encontraron registros para ese rango de fechas.'

    return render_template('consultar_registros.html', error=error, registros=registros, mensaje_no_registros=mensaje_no_registros)



@app.route('/reportes/inicio')
def inicio_reportes():
    return render_template('inicio_reportes.html')

@app.route('/reporte_general', methods=['GET', 'POST'])
def reporte_general():
    resultados = []
    error = None

    if request.method == 'POST':
        mes = request.form.get('mes')  # formato: AAAA-MM
        try:
            anio, mes_num = map(int, mes.split('-'))
        except:
            error = "Formato de mes inválido. Use AAAA-MM."
            return render_template('reporte_general.html', error=error)

        desde = date(anio, mes_num, 1)
        if mes_num == 12:
            hasta = date(anio + 1, 1, 1)
        else:
            hasta = date(anio, mes_num + 1, 1)

        trabajadores = Trabajador.query.all()

        total_horas_generales = 0

        for t in trabajadores:
            registros = RegistroHorario.query.filter(
                RegistroHorario.idtrabajador == t.id,
                RegistroHorario.fecha >= desde,
                RegistroHorario.fecha < hasta,
                RegistroHorario.horaentrada.isnot(None),
                RegistroHorario.horasalida.isnot(None)
            ).all()

            total_segundos = 0
            dependencia = None

            for r in registros:
                if dependencia is None:
                    dependencia = r.dependencia  # Tomar la dependencia del primer registro
                entrada = datetime.combine(r.fecha, r.horaentrada)
                salida = datetime.combine(r.fecha, r.horasalida)
                total_segundos += (salida - entrada).seconds

            horas = total_segundos // 3600
            minutos = (total_segundos % 3600) // 60

            total_horas_generales += total_segundos

            if dependencia is None:
                dependencia = 'Sin dependencia'

            # Solo agrego al resultado si trabajó > 0 segundos
            if total_segundos > 0:
                resultados.append({
                    'legajo': t.legajo,
                    'nombre': t.nombre,
                    'apellido': t.apellido,
                    'dependencia': dependencia,
                    'horas_trabajadas': f"{horas}h {minutos}min"
                })

        if total_horas_generales == 0:
            error = "No se encontraron horas trabajadas para ese mes."

    return render_template('reporte_general.html', resultados=resultados, error=error)



@app.route('/reportes', methods=['GET', 'POST'])
def reportes():
    error = None
    resultados = []

    if request.method == 'POST':
        desde = request.form['desde']
        hasta = request.form['hasta']
        legajo_str = request.form.get('legajo', '').strip()
        ultimos_dni = request.form.get('ultimos_dni', '').strip()

        print(f"Datos recibidos -> desde: {desde}, hasta: {hasta}, legajo: {legajo_str}, ultimos_dni: {ultimos_dni}")

        # Validar fechas
        try:
            desde_date = datetime.strptime(desde, '%Y-%m-%d').date()
            hasta_date = datetime.strptime(hasta, '%Y-%m-%d').date()
        except ValueError:
            error = 'Formato de fecha inválido. Use AAAA-MM-DD.'
            return render_template('reportes.html', error=error, resultados=resultados)

        if desde_date > hasta_date:
            error = 'La fecha "Desde" no puede ser mayor que "Hasta".'
            return render_template('reportes.html', error=error, resultados=resultados)

        # Validar legajo y DNI
        if not legajo_str or not ultimos_dni:
            error = 'Debe ingresar legajo y últimos 4 dígitos del DNI.'
            return render_template('reportes.html', error=error, resultados=resultados)

        if not ultimos_dni.isdigit() or len(ultimos_dni) != 4:
            error = 'Los últimos 4 dígitos del DNI deben ser numéricos y tener 4 dígitos.'
            return render_template('reportes.html', error=error, resultados=resultados)

        try:
            legajo = int(legajo_str)
        except ValueError:
            error = 'El legajo debe ser un número entero.'
            return render_template('reportes.html', error=error, resultados=resultados)

        trabajador = Trabajador.query.filter_by(legajo=legajo).first()
        print(f"Trabajador encontrado: {trabajador}")

        if not trabajador:
            error = 'Legajo incorrecto.'
            return render_template('reportes.html', error=error, resultados=resultados)

        print(f"Legajo: '{trabajador.legajo}'")
        print(f"DNI trabajador: '{trabajador.dni}'")
        print(f"Últimos 4 dígitos DNI ingresados: '{ultimos_dni}'")
        print(f"Comparación DNI: {trabajador.dni.endswith(ultimos_dni)}")

        if not trabajador.dni.endswith(ultimos_dni):
            error = 'Los últimos 4 dígitos del DNI no coinciden.'
            return render_template('reportes.html', error=error, resultados=resultados)

        # Buscar registros usando la relación idtrabajador
        registros = RegistroHorario.query.filter(
            RegistroHorario.idtrabajador == trabajador.id,
            RegistroHorario.fecha >= desde_date,
            RegistroHorario.fecha <= hasta_date,
        ).order_by(RegistroHorario.fecha.asc()).all()

        print(f"Cantidad registros encontrados: {len(registros)}")

        if not registros:
            error = 'No se encontraron registros para el rango seleccionado.'
            return render_template('reportes.html', error=error, resultados=resultados)

        registros_filtrados = []
        for r in registros:
            if r.horaentrada is not None and r.horasalida is not None:
                entrada = datetime.combine(r.fecha, r.horaentrada)
                salida = datetime.combine(r.fecha, r.horasalida)
                delta = salida - entrada
                horas = delta.seconds // 3600
                minutos = (delta.seconds % 3600) // 60
                horas_trabajadas = f"{horas}h {minutos}min"

                registros_filtrados.append({
                    'legajo': trabajador.legajo,
                    'nombre': trabajador.nombre,
                    'apellido': trabajador.apellido,
                    'dependencia': r.dependencia,
                    'fecha': r.fecha,
                    'horas_trabajadas': horas_trabajadas
                })

        print(f"Cantidad registros con entrada y salida: {len(registros_filtrados)}")

        if not registros_filtrados:
            error = 'No se encontraron registros con entrada y salida en el rango seleccionado.'
            return render_template('reportes.html', error=error, resultados=resultados)

        resultados = registros_filtrados

    return render_template('reportes.html', error=error, resultados=resultados)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Esto crea todas las tablas
    app.run(debug=True)
    
# Es fundamental la creación de la base de datos, con la instrucción db.create_all(), teniendo en cuenta que solo la creará si ésta no existe.
    