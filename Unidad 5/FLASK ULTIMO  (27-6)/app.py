from flask import Flask, request, render_template, session, redirect, url_for, jsonify # No sé qué onda jsonify.
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Repartidor, Sucursal, Paquete, Transporte

# Ruta para elegir tipo de usuario
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_type = request.form['user_type']
        if user_type == 'despachante':
            return redirect(url_for('login_despachante'))
        elif user_type == 'repartidor':
            return redirect(url_for('login_repartidor'))
    
    return render_template('login.html')


# Funcionalidad 1 - Acceso para los despachantes a la aplicación:
@app.route('/login_despachante', methods=['GET', 'POST'])
def login_despachante():
    if request.method == 'POST':
        # OBTENCIÓN DE DATOS DEL FORMULARIO:
        user_type = request.form.get('user_type')
        sucursal_id = request.form.get('sucursal_id')  # Asegurarse de usar "get" para obtener el VALOR.
        # Se extraen los datos del formulario enviado mediante POST.
        
        # REDIRECCIÓN SI EL TIPO DE USUARIO ES DESPACHANTE:
        if user_type == 'despachante':
            return redirect(url_for('sucursales'))
        # Se redirige al usuario a la página de SUCURSALES sin hacer otra validación.

        # VALIDACIÓN DE LA SUCURSAL:
        if not sucursal_id:
            error = "Error: Falta sucursal_id"
            return error
        # Si sucursal_id está vacío o no fue proporcionado, se devuelve una respuesta JSON con un mensaje de ERROR y el código de estado HTTP 400 (Bad Request).
        
        # ALMACENAMIENTO DE INFORMACIÓN DEL USUARIO EN LA SESIÓN:
        session['info_despachante'] = {
            'tipo': 'despachante',
            'sucursal_id': sucursal_id
        }   # Se almacena un diccionario en la sesión del usuario con la información relevante (tipo de usuario y sucursal_id).

        return redirect(url_for('registrar_paquetes'))  # Después de almacenar la información en la sesión, se redirige al usuario a la página de "Registrar Paquetes".
    
    sucursal = Sucursal.query.order_by(Sucursal.numero).all() # Obtiene la LISTA de sucursales y las pasa al template.
    # Para ello, CONSULTA la base de datos para obtenerlas, ordenadas por número de la sucursal (campo NÚMERO).
    return render_template('login_despachante.html', sucursal=sucursal) # Renderiza la plantilla.
    # Lo que se devuelve es una PÁGINA HTML y se pasa la LISTA DE SURUCRSALES OBTENIDA para que pueda ser UTILIZADA en el template (por ejemplo, un menú desplegable).


# Funcionalidad 2 - Registrar la recepción de un paquete:
@app.route('/registrar_paquetes', methods=['GET', 'POST'])
def registrar_paquetes():
    if request.method == 'POST':
        data = request.form
        if not data or not all(key in data for key in ('peso', 'nomdestinatario', 'dirdestinatario')):
            error = "Datos insuficientes"
            return error
        nuevo_paquete = Paquete(
            peso=float(data['peso']),
            nomdestinatario=data['nomdestinatario'],
            dirdestinatario=data['dirdestinatario'],
        )
        try:
            db.session.add(nuevo_paquete)
            db.session.commit()     # Este método se utiliza para confirmar todas las operaciones pendientes en una sesión de SQLAlchemy y hacer que los cambios sean permanentes en la base de datos.
        except Exception as e:
            db.session.rollback()   # Es un método utilizado en SQLAlchemy dentro de una sesión para revertir cualquier cambio no confirmado en la base de datos y volver al estado anterior a la última commit().
            error2 = "Error al registrar el paquete: " + str(e)
            return error2
        return redirect(url_for('registro_exitoso', numeroenvio=nuevo_paquete.numeroenvio, idsucursal=nuevo_paquete.idsucursal))
        #return redirect(url_for('registrar_paquetes'))
    
    paquete = Paquete.query.all()
    return render_template('registrar_paquetes.html', paquete=paquete)


@app.route('/registro_exitoso', methods=['GET', 'POST'])
def registro_exitoso():
    info_despachante = session.get('info_despachante')
    if info_despachante:
        idsucursal = info_despachante.get('sucursal_id')
    numeroenvio = request.args.get('numeroenvio')
    if request.method == 'POST':
        accion = request.form['accion']
        if accion == 'registrar_salida':
            return redirect(url_for('registrar_salida', numeroenvio=numeroenvio, idsucursal=idsucursal))
        elif accion == 'registrar_llegada':
            return redirect(url_for('registrar_llegada', idsucursal=idsucursal))
    sucursal = Sucursal.query.get(idsucursal)
    return render_template('registro_exitoso.html', sucursal=sucursal, numeroenvio=numeroenvio)



# Funcionalidad 3 - Registrar salida de un transporte:
@app.route('/registrar_salida', methods=['GET', 'POST'])
def registrar_salida():
    if request.method == 'POST':
        sucursal_id = request.form.get("sucursal_id")
        if not sucursal_id:
            error = 'Por favor selecciona una sucursal.'
            transportes = Transporte.query.all()
            sucursales = Sucursal.query.order_by(Sucursal.numero).all()
            paquetes_no_entregados = Paquete.query.filter_by(entregado=False, idrepartidor=None).all()
            return render_template('registrar_salida.html', error=error, transportes=transportes, sucursales=sucursales, paquetes_no_entregados=paquetes_no_entregados)
        
        # Guarda la sucursal de destino en la sesión y redirige a no_entregados
        session['sucursal_destino_id'] = sucursal_id
        return redirect(url_for('no_entregados'))

    # Si el método es GET, obtén la lista de transportes, sucursales y paquetes no entregados para mostrar en la plantilla
    transportes = Transporte.query.all()
    sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    paquetes_no_entregados = Paquete.query.filter_by(entregado=False, idrepartidor=None).all()
    return render_template('registrar_salida.html', transportes=transportes, sucursales=sucursales, paquetes_no_entregados=paquetes_no_entregados)


@app.route('/no_entregados', methods=['GET', 'POST'])
def no_entregados():
    idsucursal_destino = session.get('sucursal_destino_id')
    if not idsucursal_destino:
        return redirect(url_for('registrar_salida'))  # Redirige si no hay sucursal destino en la sesión

    if request.method == 'POST':
        paquete_ids = request.form.getlist('paquete_id[]')
        if not paquete_ids:
            error = "Error: debe seleccionar al menos un paquete"
            return error

        try:
            # Crear un nuevo transporte y asociar los paquetes a este transporte
            nuevo_transporte = Transporte(idsucursal=idsucursal_destino, fechahorasalida=datetime.now())
            db.session.add(nuevo_transporte)
            db.session.flush()  # Para obtener el ID del transporte recién creado

            for paquete_id in paquete_ids:
                paquete = Paquete.query.filter_by(id=paquete_id, entregado=False, idrepartidor=None).first()
                if paquete:
                    paquete.idsucursal = idsucursal_destino
                    paquete.idtransporte = nuevo_transporte.id  # Asociar el paquete con el transporte
                    db.session.add(paquete)

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            error2 = "Error al registrar la salida: " + str(e)
            return error2

        return redirect(url_for('exito_salida', idtransporte=nuevo_transporte.id))

    # Obtener los paquetes no entregados y sin repartidor asignado para mostrar en la plantilla
    paquetes_no_entregados = Paquete.query.filter_by(entregado=False, idrepartidor=None).all()
    sucursal_destino = Sucursal.query.get(idsucursal_destino)
    return render_template('no_entregados.html', paquetes_no_entregados=paquetes_no_entregados, sucursal_destino=sucursal_destino)


@app.route('/exito_salida', methods=['GET', 'POST'])
def exito_salida():
    idtransporte = request.args.get('idtransporte')
    transporte = Transporte.query.get(idtransporte)
    if not transporte:
        error = "Error: Transporte no encontrado"
        return error

    sucursal_destino = Sucursal.query.get(transporte.idsucursal)
    paquetes = Paquete.query.filter_by(idtransporte=idtransporte).all()

    return render_template('exito_salida.html', transporte=transporte, sucursal_destino=sucursal_destino, paquetes=paquetes)


# Funcionalidad 4 - Registrar llegada de un transporte:
@app.route('/registrar_llegada', methods=['GET', 'POST'])
def registrar_llegada():
    info_despachante = session.get('info_despachante', {})
    id_sucursal = info_despachante.get('sucursal_id')
    transportes = Transporte.query.filter_by(idsucursal=id_sucursal, fechahorallegada=None).all()
    print("\n\nLista de transportes:\n", transportes)

    if request.method == 'POST':
        transporte_num = request.form.get("transporte_num")
        transporte_num = int(transporte_num)
        try:
            for transporte in transportes:
                if transporte.numerotransporte == transporte_num:
                    transporte.fechahorallegada = datetime.now()
                    db.session.commit()
        except Exception as e:
            db.session.rollback()
            error = "Error al registrar la llegada: " + str(e)
            return error

        return redirect(url_for('exito_llegada', transporte_num=transporte_num, id_sucursal=id_sucursal))

    return render_template('registrar_llegada.html', idsucursal=id_sucursal, transportes=transportes)

@app.route('/exito_llegada', methods=['GET', 'POST'])
def exito_llegada():
    transporte_num = request.args.get('transporte_num')
    print("\nXD", transporte_num)
    transporte = Transporte.query.filter_by(numerotransporte=transporte_num).first()
    if not transporte:
        error = "Error: Transporte no encontrado"
        return error

    id_sucursal = request.args.get('id_sucursal')
    sucursal_llegada = Sucursal.query.filter_by(id=id_sucursal).first()

    return render_template('exito_llegada.html', transporte=transporte, sucursal_llegada=sucursal_llegada)



# Funcionalidad 5 - Asignar paquetes a un repartidor:
@app.route('/asignar_paquetes', methods=['GET', 'POST'])
def asignar_paquetes():
    if request.method == 'POST':
        repartidor_id = request.form['repartidor_id']
        paquete_ids = request.form.getlist('paquete_ids')
        for paquete_id in paquete_ids:
            paquete = Paquete.query.get(paquete_id)
            paquete.idrepartidor = repartidor_id
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            error = "Error al registrar la llegada: " + str(e)
            return error
        return redirect(url_for('asignar_paquetes'))
    
    repartidores = Repartidor.query.all()
    paquetes = Paquete.query.filter_by(entregado=False, idrepartidor=None).all()
    return render_template('asignar_paquetes.html', repartidores=repartidores, paquetes=paquetes, error=error)


# Funcionalidad 6 - Acceso para los repartidores a la aplicación
@app.route('/login_repartidor', methods=['GET', 'POST'])
def login_repartidor():
    if request.method == 'POST':
        numero = request.form.get('numero')
        dni = request.form.get('dni')
        
        # Verificación básica de credenciales
        if not numero or not dni:
            return jsonify({'error': 'Credenciales incorrectas'}), 401
        
        repartidor = Repartidor.query.filter_by(numero=numero, dni=dni).first()
        
        if repartidor:
            session['user_info'] = {
                'tipo': 'repartidor',
                'repartidor_id': repartidor.id
            }
            return redirect(url_for('entregar_paquete'))  # Redirige al repartidor a la página de "Registrar Entrega"
        else:
            return jsonify({'error': 'Credenciales incorrectas'}), 401
    
    return render_template('login_repartidor.html')




# Funcionalidad 7 - Registrar la entrega de un paquete:
@app.route('/entregar_paquete', methods=['GET', 'POST'])
def entregar_paquete():
    if request.method == 'POST':
        paquete_id = request.form['paquete_id']
        entregado = request.form['entregado']
        observaciones = request.form['observaciones']
        paquete = Paquete.query.get(paquete_id)
        paquete.entregado = (entregado == 'true')
        paquete.observaciones = observaciones
        if entregado == 'true':
            paquete.nomdestinatario = request.form['nomdestinatario']
            paquete.dnidestinatario = request.form['dnidestinatario']
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
        return redirect(url_for('entregar_paquete'))
    
    repartidor_id = request.args.get('repartidor_id')
    if repartidor_id:
        paquetes = Paquete.query.filter_by(idrepartidor=repartidor_id, entregado=False).all()
    else:
        paquetes = Paquete.query.filter_by(entregado=False).all()
    
    return render_template('entregar_paquete.html', paquetes=paquetes)





# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('user_info', None)
    return redirect(url_for('login'))


@app.route('/sucursales', methods=['GET', 'POST'])
def sucursales():
    if request.method == 'POST':
        data = request.form
        if not data or not all(key in data for key in ('numero', 'provincia', 'localidad', 'direccion')):
            return jsonify({'error': 'Datos insuficientes'}), 400
        nueva_sucursal = Sucursal(
            numero=data['numero'],
            provincia=data['provincia'],
            localidad=data['localidad'],
            direccion=data['direccion']
        )
        try:
            db.session.add(nueva_sucursal)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
        return redirect(url_for('sucursales'))
    
    sucursales = Sucursal.query.all()
    return render_template('sucursales.html', sucursales=sucursales)


@app.route('/repartidores', methods=['GET', 'POST'])
def repartidores():
    if request.method == 'POST':
        data = request.form
        if not data or not all(key in data for key in ('nombre', 'dni', 'idsucursal', 'numero')):
            return jsonify({'error': 'Datos insuficientes'}), 400
        nuevo_repartidor = Repartidor(
            nombre=data['nombre'],
            dni=data['dni'],
            idsucursal=int(data['idsucursal']),
            numero=data['numero'],
        )
        try:
            db.session.add(nuevo_repartidor)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
        return redirect(url_for('repartidores'))
    
    repartidores = Repartidor.query.all()
    sucursales = Sucursal.query.all()  # Obtener las sucursales y pasarlas a la plantilla
    return render_template('repartidores.html', repartidores=repartidores, sucursales=sucursales)

if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()  # Esto crea todas las tablas
    
# Es fundamental la creación de la base de datos, con la instrucción db.create_all(), teniendo en cuenta que solo la creará si ésta no existe.
    
