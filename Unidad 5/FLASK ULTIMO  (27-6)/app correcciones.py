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



@app.route('/opciones_despachante', methods=['GET', 'POST'])
def opciones_despachante():
    if request.method == 'POST':
        user_type = request.form.get('user_type')
        if user_type == 'Registrar paquetes':
            return redirect(url_for('registrar_paquetes'))
        elif user_type == 'Asignar paquetes':
            sucursal_id = session.get('info_despachante')['sucursal_id']
            return redirect(url_for('asignar_paquetes', sucursal_id=sucursal_id))
        else:
            return render_template('opciones_despachante.html', error="Opción no válida, por favor seleccione una opción válida.")
    return render_template('opciones_despachante.html')


# Funcionalidad 1 - Acceso para los despachantes a la aplicación:
@app.route('/login_despachante', methods=['GET', 'POST'])
def login_despachante():
    if request.method == 'POST':
        # OBTENCIÓN DE DATOS DEL FORMULARIO:
        user_type = request.form.get('user_type')
        sucursal_id = request.form.get('sucursal_id')  # Asegurarse de usar "get" para obtener el VALOR.
        # Se extraen los datos del formulario enviado mediante POST.
        
        '''
        # REDIRECCIÓN SI EL TIPO DE USUARIO ES DESPACHANTE:
        if user_type == 'despachante':
            return redirect(url_for('sucursales'))
        # Se redirige al usuario a la página de SUCURSALES sin hacer otra validación.
        '''
        # VALIDACIÓN DE LA SUCURSAL:
        if not sucursal_id:
            return jsonify({'error': 'Falta sucursal_id'}), 400
        # Si sucursal_id está vacío o no fue proporcionado, se devuelve una respuesta JSON con un mensaje de ERROR y el código de estado HTTP 400 (Bad Request).
        
        # ALMACENAMIENTO DE INFORMACIÓN DEL USUARIO EN LA SESIÓN:
        session['info_despachante'] = {
            'tipo': 'despachante',
            'sucursal_id': sucursal_id
        }   # Se almacena un diccionario en la sesión del usuario con la información relevante (tipo de usuario y sucursal_id).
        return redirect(url_for('opciones_despachante',sucursalID=sucursal_id))  # Después de almacenar la información en la sesión, se redirige al usuario a la página de "Registrar Paquetes".
    
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
            sucursales = Sucursal.query.order_by(Sucursal.numero).all()
            paquetes_no_entregados = Paquete.query.filter_by(entregado=False, idrepartidor=None, idtransporte=None).all() # 25/6 añadí idtransporte=None para que sólo pida los paquetes SIN TRANSPORTE ni repartidor ASIGNADOS.
            return render_template('registrar_salida.html', error=error, sucursales=sucursales, paquetes_no_entregados=paquetes_no_entregados)
        
        # Guarda la sucursal de destino en la sesión y redirige a no_entregados
        session['sucursal_destino_id'] = sucursal_id
        return redirect(url_for('no_entregados')) 


    sucursales = Sucursal.query.order_by(Sucursal.numero).all()
    paquetes_no_entregados = Paquete.query.filter_by(entregado=False, idrepartidor=None, idtransporte=None).all() 
    return render_template('registrar_salida.html', sucursales=sucursales, paquetes_no_entregados=paquetes_no_entregados)


@app.route('/no_entregados', methods=['GET', 'POST'])
def no_entregados():
    transportes = Transporte.query.first() # 25/6
    print("\n\nLista de transportes: ", transportes, "\n")
    idsucursal_destino = session.get('sucursal_destino_id')
    if not idsucursal_destino:
        return redirect(url_for('registrar_salida'))  # Redirige si no hay sucursal destino en la sesión

    if request.method == 'POST':
        paquete_ids = request.form.getlist('paquete_id[]')
        if not paquete_ids:
            error = "Error: debe seleccionar al menos un paquete"
            return error
        try:
            for paquete_id in paquete_ids:
                paquete = Paquete.query.filter_by(id=paquete_id, entregado=False, idrepartidor=None, idtransporte=None).first() # 26/6 le quité el idtransporte=None para que sólo pida los paquetes sin entregar y sin repartidor ASIGNADOS.
                if paquete:
                    paquete.idsucursal = idsucursal_destino
                    paquete.idtransporte = transportes.id  # 25/6 Asociar el paquete con el transporte - permite actualizar la lista de paquetes SIN TRANSPORTE ASIGNADO.
                    transportes.fechahorasalida = datetime.now() # 25/6 genera la fecha de salida automáticamente.
                    print("ID transporte:", transportes.id, "\n")
                    print("ID paquete:", paquete.id, "\n")
                    db.session.add(paquete)

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            error2 = "Error al registrar la salida: " + str(e)
            return error2

        for paquete_id in paquete_ids:
            print("Estado de entrega de paquete marcado:", paquete.entregado)

        return redirect(url_for('exito_salida', idtransporte=transportes.id))

    # Obtener los paquetes no entregados y sin repartidor asignado para mostrar en la plantilla
    paquetes_no_entregados = Paquete.query.filter_by(entregado=False, idrepartidor=None, idtransporte=None).all() # 25/6 agregué idtransporte=None para que sólo muestre los paquetes SIN TRANSPORTE, además de las otras condiciones.

    sucursal_destino = Sucursal.query.get(idsucursal_destino)
    return render_template('no_entregados.html', paquetes_no_entregados=paquetes_no_entregados, sucursal_destino=sucursal_destino)



@app.route('/exito_salida', methods=['GET', 'POST'])
def exito_salida():
    idtransporte = request.args.get('idtransporte')
    transporte = Transporte.query.get(idtransporte)
    if not transporte:
        error = "Error: Transporte no encontrado"
        return error

    sucursal_destino = Sucursal.query.get(transporte.id)
    idsucursal_destino = sucursal_destino.id
    
    paquetes = Paquete.query.filter_by(idtransporte=idtransporte, entregado=False, idrepartidor=None).all() # 25/6 cambié el filtro para que sólo se vean aquellos paquetes con el nuevo TRANSPORTE ASIGNADO, pero que aún no han sido entregados ni tienen un repartidor asignado.

    return render_template('exito_salida.html', transporte=transporte, sucursal_destino=sucursal_destino, paquetes=paquetes)


# Funcionalidad 4 - Registrar llegada de un transporte:
@app.route('/registrar_llegada', methods=['GET', 'POST'])
def registrar_llegada():
    info_despachante = session.get('info_despachante', {})
    id_sucursal = info_despachante.get('sucursal_id')
    #transportes = Transporte.query.filter_by(idsucursal=id_sucursal, fechahorallegada=None).all()
    #transportes = Transporte.query.filter_by(idsucursal=id_sucursal).all()
    transportes = Transporte.query.filter_by(fechahorallegada=None).all()

    #print("\n\nLista de transportes: ", transportes, "\n")
    
    for transporte in transportes:
        transporte.idsucursal = id_sucursal
        #transporte.fechahorallegada = None # 26/6 para "reiniciar" la fecha de llegada y se muestre en el listado y que tenga la misma sucursal que la que se eligió.
        print("\nFecha de llegada: ", transporte.fechahorallegada, "\n")
    #print("\n\nLista de transportes:\n", transportes)
    

    if request.method == 'POST':
        transporte_num = request.form.get("transporte_num")
        transporte_num = int(transporte_num)
        print("\nNúmero de transporte:", transporte_num, "\n")
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
    #print("\nXD", transporte_num)
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
        repartidor_id = request.form.get('repartidor_id')
        paquete_ids = request.form.getlist('paquete_ids')
        sucursal_id= request.args.get('sucursal_id')
        print("Sucursal seleccionada en el despachante: ", sucursal_id, "\n")
        for paquete in paquete_ids:
            print("\nPaquete seleccionado: ", paquete, "\n")
        
        for paquete_id in paquete_ids:
            paquete = Paquete.query.get(paquete_id)
            paquete.idrepartidor = repartidor_id
            print("\nID DEL REPARTIDOR: ", paquete.idrepartidor, "\n") # SÍ SE GUARDA CORRECTAMENTE.
        
        if not paquete_ids:
            error = "Error: debe seleccionar al menos un paquete"
            return error

        try:
            db.session.commit()
            return render_template('paquete_asignado.html')
        except Exception as e:
            db.session.rollback()
            return render_template('asignacion_error.html') #
    
    # Obtener la sucursal del despachante desde la sesión
    sucursal_id = session.get('info_despachante')['sucursal_id']
    print("\n\nASIGNAR - PAQUETES - Sucursal de destino: ", sucursal_id, "\n") # SÍ SE GUARDA
    
    # Filtrar repartidores y paquetes según la sucursal
    repartidores = Repartidor.query.filter_by(idsucursal=sucursal_id).all()
    paquetes = Paquete.query.filter_by(entregado=False, idrepartidor=None).all()
    
    return render_template('asignar_paquetes.html', repartidores=repartidores, paquetes=paquetes)


# Funcionalidad 6 - Acceso para los repartidores a la aplicación
@app.route('/login_repartidor', methods=['GET', 'POST'])
def login_repartidor():
    if request.method == 'POST':
        numero = request.form.get('numero')
        dni = request.form.get('dni')
        print("LOGIN REPARTIDOR - \nDNI: ", dni, "\n")
        print("LOGIN REPARTIDOR - \nNUMERO: ", numero, "\n")
        
        # Ejemplo de verificación básica de credenciales
        
        repartidor = Repartidor.query.filter_by(numero=numero, dni=dni).first()
        if repartidor:
            print("ID del repartidor: ", repartidor.id, "\n")
        
        if repartidor:
            session['user_info'] = {
                'tipo': 'repartidor',
                'repartidor_id': repartidor.id
            }
            print("\nLOGIN REPARTIDOR - ID DEL REPARTIDOR: ", repartidor.id, "\n") # SÍ SE GUARDA CORRECTAMENTE.

            return redirect(url_for('entregar_paquete', repartidor_id=repartidor.id))
        else:
            return render_template('credenciales_incorrectas.html')
    
    return render_template('login_repartidor.html')



# Funcionalidad 7 - Registrar la entrega de un paquete:
@app.route('/entregar_paquete', methods=['GET', 'POST'])
def entregar_paquete():
    repartidor_id = request.args.get('repartidor_id')
    print("\nENTREGAR PAQUETE - ID DEL REPARTIDOR: ", repartidor_id, "\n")
    print("\nTIPO DE DATO REPARTIDOR", type(repartidor_id), "\n")
    repartidor_id = int(repartidor_id)
    success = None
    error = None

    if request.method == 'POST':
        paquete_id = request.form['paquete_id']
        entregado = request.form['entregado']
        observaciones = request.form['observaciones']
        paquete = Paquete.query.get(paquete_id)
        print("\nENTREGAR PAQUETE - ID DEL PAQUETE: ", paquete.idrepartidor, "\n") #
        print("\nTIPO DE DATO PAQUETE", type(paquete.idrepartidor), "\n")
        idpaquete_repartidor = paquete.idrepartidor
        
        if not paquete:
            error = 'Número de envío no encontrado'
        else:
            if idpaquete_repartidor != repartidor_id:
                error = 'Paquete no asignado a este repartidor'
            else:
                paquete.entregado = (entregado == 'true')
                paquete.observaciones = observaciones               
                try:
                    db.session.commit()
                    success = 'Información de entrega actualizada'
                except Exception as e:
                    db.session.rollback()
                    error = f'Error al actualizar la información: {e}'
        
        return render_template('entregar_paquete.html', paquetes=Paquete.query.filter_by(idrepartidor=repartidor_id, entregado=False).all(), success=success, error=error)
    
    repartidor_id = request.args.get('repartidor_id', 1)  # Este valor debe obtenerse dinámicamente
    paquetes = Paquete.query.filter_by(idrepartidor=repartidor_id, entregado=False).all()
    for paquete in paquetes:
        print("\nENTREGAR PAQUETE - ID DEL REPARTIDOR ASIGNADO AL PAQUETE: ", paquete.idrepartidor, "\n") #
    return render_template('entregar_paquete.html', paquetes=paquetes, idrepartidor=repartidor_id)


# AGREGAR TRANSPORTE
@app.route('/transportes', methods=['GET', 'POST'])
def transportes():
    if request.method == 'POST':
        data = request.form
        if not data or not all(key in data for key in ('numerotransporte', 'fechahorasalida', 'idsucursal')):
            return jsonify({'error': 'Datos insuficientes'}), 400
        try:
            # Convertir la fecha y hora de salida de string a datetime
            fechahorasalida = datetime.strptime(data['fechahorasalida'], '%Y-%m-%dT%H:%M')
            
            # Verificar si se proporciona la fecha y hora de llegada
            fechahorallegada = datetime.strptime(data['fechahorallegada'], '%Y-%m-%dT%H:%M') if data.get('fechahorallegada') else None
            
            nuevo_transporte = Transporte(
                numerotransporte=data['numerotransporte'],
                fechahorasalida=fechahorasalida,
                fechahorallegada=fechahorallegada,
                idsucursal=int(data['idsucursal'])
            )
            db.session.add(nuevo_transporte)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
        return redirect(url_for('transportes'))
    
    transportes = Transporte.query.all()
    sucursales = Sucursal.query.all()  # Obtener las sucursales y pasarlas a la plantilla
    return render_template('transportes.html', transportes=transportes, sucursales=sucursales)



if __name__ == '__main__':
    app.run(debug=True)
    with app.app_context():
        db.create_all()  # Esto crea todas las tablas
    
# Es fundamental la creación de la base de datos, con la instrucción db.create_all(), teniendo en cuenta que solo la creará si ésta no existe.
    
