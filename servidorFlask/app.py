from flask import Flask, request, jsonify, session
from flask_cors import CORS
from werkzeug.security import check_password_hash
from models import (
    db, ma,
    Propietario, PropietarioSchema,
    Apartamento, ApartamentoSchema,
    Horario, HorarioSchema,
    Empleado, EmpleadoSchema,
    Cliente, ClienteSchema,
    Reserva, ReservaSchema,
    Pulsera, PulseraSchema,
    Acceso, AccesoSchema,
    EventoFichaje, EventoFichajeSchema
)
import config

app = Flask(__name__)
app.secret_key = 'clave-muy-secreta'  # Reemplázala en producción
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

# Inicialización de extensiones
db.init_app(app)
ma.init_app(app)

# Permitir CORS para desarrollo
CORS(app)

# Función reutilizable para registrar endpoints CRUD
def register_endpoints(model, schema, schema_many, route_name):
    app.add_url_rule(
        f'/{route_name}',
        endpoint=f'{route_name}_get_all',
        view_func=lambda: schema_many.jsonify(model.query.all()),
        methods=['GET']
    )

    app.add_url_rule(
        f'/{route_name}/<int:id>',
        endpoint=f'{route_name}_get_one',
        view_func=lambda id: schema.jsonify(model.query.get_or_404(id)),
        methods=['GET']
    )

    def add():
        data = request.json
        item = model(**data)
        db.session.add(item)
        db.session.commit()
        return schema.jsonify(item), 201

    app.add_url_rule(
        f'/{route_name}',
        endpoint=f'{route_name}_add',
        view_func=add,
        methods=['POST']
    )

    def update(id):
        item = model.query.get_or_404(id)
        for key, value in request.json.items():
            setattr(item, key, value)
        db.session.commit()
        return schema.jsonify(item)

    app.add_url_rule(
        f'/{route_name}/<int:id>',
        endpoint=f'{route_name}_update',
        view_func=update,
        methods=['PUT']
    )

    def delete(id):
        item = model.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return '', 204

    app.add_url_rule(
        f'/{route_name}/<int:id>',
        endpoint=f'{route_name}_delete',
        view_func=delete,
        methods=['DELETE']
    )

# Registro de todos los modelos y esquemas con sus endpoints CRUD
register_endpoints(Propietario, PropietarioSchema(), PropietarioSchema(many=True), 'propietarios')
register_endpoints(Apartamento, ApartamentoSchema(), ApartamentoSchema(many=True), 'apartamentos')
register_endpoints(Horario, HorarioSchema(), HorarioSchema(many=True), 'horarios')
register_endpoints(Empleado, EmpleadoSchema(), EmpleadoSchema(many=True), 'empleados')
register_endpoints(Cliente, ClienteSchema(), ClienteSchema(many=True), 'clientes')
register_endpoints(Reserva, ReservaSchema(), ReservaSchema(many=True), 'reservas')
register_endpoints(Pulsera, PulseraSchema(), PulseraSchema(many=True), 'pulseras')
register_endpoints(Acceso, AccesoSchema(), AccesoSchema(many=True), 'accesos')
register_endpoints(EventoFichaje, EventoFichajeSchema(), EventoFichajeSchema(many=True), 'eventos_fichaje')

# Endpoint personalizado para login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    dni = data.get('dni')
    password = data.get('password')

    empleado = Empleado.query.filter_by(dni=dni).first()
    if not empleado:
        return jsonify({'error': 'DNI no encontrado'}), 404

    if not check_password_hash(empleado.password, password):
        return jsonify({'error': 'Contraseña incorrecta'}), 401

    session['empleado_id'] = empleado.empleado_id
    return jsonify({'message': 'Login correcto'})

if __name__ == '__main__':
    app.run(debug=True)
