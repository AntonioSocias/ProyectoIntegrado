# app.py ajustado con comentarios y mejoras
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from modelos import (
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


# Inicialización de extensiones
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Función reutilizable para registrar endpoints CRUD

def register_endpoints(model, schema, schema_many, route_name):
    @app.route(f'/{route_name}', methods=['GET'])
    def get_all():
        items = model.query.all()
        return schema_many.jsonify(items)

    @app.route(f'/{route_name}/<int:id>', methods=['GET'])
    def get_one(id):
        item = model.query.get_or_404(id)
        return schema.jsonify(item)

    @app.route(f'/{route_name}', methods=['POST'])
    def add():
        data = request.json
        item = model(**data)
        db.session.add(item)
        db.session.commit()
        return schema.jsonify(item), 201

    @app.route(f'/{route_name}/<int:id>', methods=['PUT'])
    def update(id):
        item = model.query.get_or_404(id)
        for key, value in request.json.items():
            setattr(item, key, value)
        db.session.commit()
        return schema.jsonify(item)

    @app.route(f'/{route_name}/<int:id>', methods=['DELETE'])
    def delete(id):
        item = model.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return '', 204

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
