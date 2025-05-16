from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# -------------------- MODELOS --------------------

class Propietario(db.Model):
    propietario_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    telefono = db.Column(db.String(20))
    email = db.Column(db.String(100))
    direccion = db.Column(db.Text)

class Apartamento(db.Model):
    apartamento_id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(10), nullable=False)
    planta = db.Column(db.Integer)
    bloque = db.Column(db.String(10))
    estado = db.Column(db.String(20))
    propietario_id = db.Column(db.Integer, db.ForeignKey('propietario.propietario_id'))

class Horario(db.Model):
    horario_id = db.Column(db.Integer, primary_key=True)
    dia_semana = db.Column(db.String(10), nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False)
    hora_fin = db.Column(db.Time, nullable=False)

class Empleado(db.Model):
    empleado_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    puesto = db.Column(db.String(50))
    email = db.Column(db.String(100))
    horario_id = db.Column(db.Integer, db.ForeignKey('horario.horario_id'))
    password = db.Column(db.String(128))

class Cliente(db.Model):
    cliente_id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    dni = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100))
    telefono = db.Column(db.String(20))

class Reserva(db.Model):
    reserva_id = db.Column(db.Integer, primary_key=True)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=False)
    apartamento_id = db.Column(db.Integer, db.ForeignKey('apartamento.apartamento_id'))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.cliente_id'))

class Pulsera(db.Model):
    pulsera_id = db.Column(db.Integer, primary_key=True)
    codigo_uid = db.Column(db.String(100), unique=True, nullable=False)
    tipo = db.Column(db.String(50))
    activa = db.Column(db.Boolean, default=True)

class Acceso(db.Model):
    acceso_id = db.Column(db.Integer, primary_key=True)
    fecha_hora = db.Column(db.DateTime, nullable=False)
    tipo_acceso = db.Column(db.String(50))
    apartamento_id = db.Column(db.Integer, db.ForeignKey('apartamento.apartamento_id'))
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.empleado_id'))
    pulsera_id = db.Column(db.Integer, db.ForeignKey('pulsera.pulsera_id'))

class EventoFichaje(db.Model):
    evento_id = db.Column(db.Integer, primary_key=True)
    fecha_hora = db.Column(db.DateTime, nullable=False)
    tipo_evento = db.Column(db.String(50))
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.empleado_id'))

# -------------------- ESQUEMAS --------------------

class PropietarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Propietario
        load_instance = True

class ApartamentoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Apartamento
        load_instance = True

class HorarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Horario
        load_instance = True

class EmpleadoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Empleado
        load_instance = True

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
        load_instance = True

class ReservaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reserva
        load_instance = True

class PulseraSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pulsera
        load_instance = True

class AccesoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Acceso
        load_instance = True

class EventoFichajeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EventoFichaje
        load_instance = True
