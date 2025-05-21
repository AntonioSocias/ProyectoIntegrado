from flask import request, jsonify
from datetime import datetime, date
from werkzeug.security import check_password_hash
from models import (
    db,
    Empleado, EventoFichaje, EventoFichajeSchema,
    Apartamento, ApartamentoSchema,
    Acceso, AccesoSchema,
    Pulsera
)

def register_custom_endpoints(app):

    # Login de empleado con id_usuario y password
    @app.route('/login', methods=['POST'])
    def login():
        data = request.json
        usuario = data.get('id_usuario')
        password = data.get('password')

        empleado = Empleado.query.filter_by(id_usuario=usuario).first()
        if not empleado:
            return jsonify({'error': 'Usuario no encontrado'}), 404

        print("valor empleado hash: ", empleado.password)
        print("valor pasada hash: ", password)

        if not check_password_hash(empleado.password, password):
            return jsonify({'error': 'Contraseña incorrecta'}), 401

        return jsonify({'message': 'Login correcto', 'empleado_id': empleado.id})

    # Fichaje de entrada o salida del empleado
    @app.route('/empleados/<int:id_empleado>/fichar', methods=['POST'])
    def fichar_empleado(id_empleado):
        data = request.json
        tipo = data.get('tipo')  # Debe ser "entrada" o "salida"

        if tipo not in ['entrada', 'salida']:
            return jsonify({'error': 'Tipo no válido'}), 400

        fichaje = EventoFichaje(
            id_empleado=id_empleado,
            tipo=tipo,
            fecha_hora=datetime.now()
        )
        db.session.add(fichaje)
        db.session.commit()

        return jsonify({'message': f'{tipo.capitalize()} registrada con éxito'})

    # Obtener fichajes de un empleado
    @app.route('/empleados/<int:id_empleado>/fichajes', methods=['GET'])
    def obtener_fichajes(id_empleado):
        fichajes = EventoFichaje.query.filter_by(id_empleado=id_empleado).all()
        return EventoFichajeSchema(many=True).jsonify(fichajes)

    # Obtener apartamentos disponibles (estado = 'disponible')
    @app.route('/apartamentos/disponibles', methods=['GET'])
    def apartamentos_disponibles():
        disponibles = Apartamento.query.filter_by(estado='disponible').all()
        return ApartamentoSchema(many=True).jsonify(disponibles)

    # Obtener accesos realizados hoy
    @app.route('/accesos/hoy', methods=['GET'])
    def accesos_hoy():
        inicio = datetime.combine(date.today(), datetime.min.time())
        fin = datetime.combine(date.today(), datetime.max.time())
        accesos = Acceso.query.filter(Acceso.fecha.between(inicio, fin)).all()
        return AccesoSchema(many=True).jsonify(accesos)

    # Verificar si una pulsera existe y está activa
    @app.route('/pulseras/verificar/<string:uid>', methods=['GET'])
    def verificar_pulsera(uid):
        pulsera = Pulsera.query.filter_by(uid=uid).first()
        if not pulsera:
            return jsonify({'valida': False, 'mensaje': 'Pulsera no encontrada'}), 404

        return jsonify({
            'valida': True,
            'estado': pulsera.estado,
            'id_usuario': pulsera.id_usuario
        })
