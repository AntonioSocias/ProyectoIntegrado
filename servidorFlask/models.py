from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

# -------------------- MODELOS --------------------

class Propietario(db.Model):
    id_propietario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    dni = db.Column(db.String)
    telefono = db.Column(db.String)

class GrupoGestor(db.Model):
    id_grupo = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    contacto = db.Column(db.String)

class Cliente(db.Model):
    id_cliente = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    dni = db.Column(db.String)
    telefono = db.Column(db.String)

class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_apartamento = db.Column(db.Integer, db.ForeignKey('apartamento.id'))
    f_inicio = db.Column(db.Date)
    f_fin = db.Column(db.Date)
    estado = db.Column(db.String)
    nombre_reserva = db.Column(db.String)
    num_personas = db.Column(db.Integer)

class Apartamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero_apartamento = db.Column(db.String)
    id_propietario = db.Column(db.Integer, db.ForeignKey('propietario.id_propietario'))
    id_grupo_gestor = db.Column(db.Integer, db.ForeignKey('grupo_gestor.id_grupo'))
    estado = db.Column(db.String)
    id_reserva = db.Column(db.Integer, db.ForeignKey('reserva.id'))

class Horario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    hora_entrada = db.Column(db.Time)
    hora_salida = db.Column(db.Time)
    dias_semana = db.Column(db.String)

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    rol = db.Column(db.String)
    id_usuario = db.Column(db.String)
    password = db.Column(db.String)
    telefono = db.Column(db.String)
    id_horario = db.Column(db.Integer, db.ForeignKey('horario.id'))

class Pulsera(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String)
    estado = db.Column(db.String)
    id_usuario = db.Column(db.Integer)

class Zona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String)
    descripcion = db.Column(db.String)

class Acceso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_zona = db.Column(db.Integer, db.ForeignKey('zona.id'))
    resultado = db.Column(db.Enum('valido', 'rechazado', name='resultado_acceso'))
    id_pulsera = db.Column(db.Integer, db.ForeignKey('pulsera.id'))
    fecha = db.Column(db.DateTime)

class EventoFichaje(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleado.id'))
    tipo = db.Column(db.Enum('entrada', 'salida', name='tipo_fichaje'))
    fecha_hora = db.Column(db.DateTime)

class Incidencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    descripcion = db.Column(db.Text)
    estado = db.Column(db.String)
    fecha = db.Column(db.DateTime)
    id_apartamento = db.Column(db.Integer, db.ForeignKey('apartamento.id'))

class LogEventos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tabla_afectada = db.Column(db.String)
    operacion = db.Column(db.String)
    usuario = db.Column(db.String)
    fecha = db.Column(db.DateTime)
    descripcion = db.Column(db.Text)

# -------------------- ESQUEMAS --------------------

class PropietarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Propietario
        load_instance = True

class GrupoGestorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GrupoGestor
        load_instance = True

class ClienteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
        load_instance = True

class ReservaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reserva
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

class PulseraSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pulsera
        load_instance = True

class ZonaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Zona
        load_instance = True

class AccesoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Acceso
        load_instance = True

class EventoFichajeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = EventoFichaje
        load_instance = True

class IncidenciaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Incidencia
        load_instance = True

class LogEventosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = LogEventos
        load_instance = True
