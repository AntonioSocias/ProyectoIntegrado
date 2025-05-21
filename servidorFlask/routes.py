from flask import request, jsonify
from models import db, \
    Propietario, PropietarioSchema, \
    GrupoGestor, GrupoGestorSchema, \
    Cliente, ClienteSchema, \
    Reserva, ReservaSchema, \
    Apartamento, ApartamentoSchema, \
    Horario, HorarioSchema, \
    Empleado, EmpleadoSchema, \
    Pulsera, PulseraSchema, \
    Zona, ZonaSchema, \
    Acceso, AccesoSchema, \
    EventoFichaje, EventoFichajeSchema, \
    Incidencia, IncidenciaSchema, \
    LogEventos, LogEventosSchema

def register_crud_endpoints(app):
    def create_crud(model, schema, schema_many, route):
        # GET todos
        app.add_url_rule(
            f'/{route}',
            view_func=lambda: schema_many.jsonify(model.query.all()),
            methods=['GET'],
            endpoint=f'{route}_get_all'
        )

        # GET uno por ID
        app.add_url_rule(
            f'/{route}/<int:id>',
            view_func=lambda id: schema.jsonify(model.query.get_or_404(id)),
            methods=['GET'],
            endpoint=f'{route}_get_one'
        )

        # POST crear nuevo
        def create():
            data = request.json
            item = model(**data)
            db.session.add(item)
            db.session.commit()
            return schema.jsonify(item), 201

        app.add_url_rule(
            f'/{route}',
            view_func=create,
            methods=['POST'],
            endpoint=f'{route}_create'
        )

        # PUT actualizar
        def update(id):
            item = model.query.get_or_404(id)
            for key, value in request.json.items():
                setattr(item, key, value)
            db.session.commit()
            return schema.jsonify(item)

        app.add_url_rule(
            f'/{route}/<int:id>',
            view_func=update,
            methods=['PUT'],
            endpoint=f'{route}_update'
        )

        # DELETE eliminar
        def delete(id):
            item = model.query.get_or_404(id)
            db.session.delete(item)
            db.session.commit()
            return '', 204

        app.add_url_rule(
            f'/{route}/<int:id>',
            view_func=delete,
            methods=['DELETE'],
            endpoint=f'{route}_delete'
        )

    # Registrar todos los modelos
    create_crud(Propietario, PropietarioSchema(), PropietarioSchema(many=True), 'propietarios')
    create_crud(GrupoGestor, GrupoGestorSchema(), GrupoGestorSchema(many=True), 'grupos_gestor')
    create_crud(Cliente, ClienteSchema(), ClienteSchema(many=True), 'clientes')
    create_crud(Reserva, ReservaSchema(), ReservaSchema(many=True), 'reservas')
    create_crud(Apartamento, ApartamentoSchema(), ApartamentoSchema(many=True), 'apartamentos')
    create_crud(Horario, HorarioSchema(), HorarioSchema(many=True), 'horarios')
    create_crud(Empleado, EmpleadoSchema(), EmpleadoSchema(many=True), 'empleados')
    create_crud(Pulsera, PulseraSchema(), PulseraSchema(many=True), 'pulseras')
    create_crud(Zona, ZonaSchema(), ZonaSchema(many=True), 'zonas')
    create_crud(Acceso, AccesoSchema(), AccesoSchema(many=True), 'accesos')
    create_crud(EventoFichaje, EventoFichajeSchema(), EventoFichajeSchema(many=True), 'eventos_fichaje')
    create_crud(Incidencia, IncidenciaSchema(), IncidenciaSchema(many=True), 'incidencias')
    create_crud(LogEventos, LogEventosSchema(), LogEventosSchema(many=True), 'log_eventos')
