from flask import Flask, request, jsonify
from flask_cors import CORS
from models import (
    db, ma,  # importar instancias ya inicializadas
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
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS

# Aquí sí se inicializan las extensiones con la app
db.init_app(app)
ma.init_app(app)
ma.init_app(app)

CORS(app)

# Función reutilizable para registrar endpoints CRUD
def register_endpoints(model, schema, schema_many, route_name):
    # GET all
    app.add_url_rule(
        f'/{route_name}',
        endpoint=f'{route_name}_get_all',
        view_func=lambda: schema_many.jsonify(model.query.all()),
        methods=['GET']
    )

    # GET by ID
    app.add_url_rule(
        f'/{route_name}/<int:id>',
        endpoint=f'{route_name}_get_one',
        view_func=lambda id: schema.jsonify(model.query.get_or_404(id)),
        methods=['GET']
    )

    # POST
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

    # PUT
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

    # DELETE
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

if __name__ == '__main__':
    app.run(debug=True)
