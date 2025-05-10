from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Date, Time, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Propietario(Base):
    __tablename__ = 'propietario'
    propietario_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    dni = Column(String(20), unique=True, nullable=False)
    telefono = Column(String(20))
    email = Column(String(100))
    direccion = Column(Text)

class Apartamento(Base):
    __tablename__ = 'apartamento'
    apartamento_id = Column(Integer, primary_key=True)
    numero = Column(String(10), nullable=False)
    planta = Column(Integer)
    bloque = Column(String(10))
    estado = Column(String(20))
    propietario_id = Column(Integer, ForeignKey('propietario.propietario_id'))

class Horario(Base):
    __tablename__ = 'horario'
    horario_id = Column(Integer, primary_key=True)
    dia_semana = Column(String(10), nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fin = Column(Time, nullable=False)

class Empleado(Base):
    __tablename__ = 'empleado'
    empleado_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    dni = Column(String(20), unique=True, nullable=False)
    puesto = Column(String(50))
    email = Column(String(100))
    horario_id = Column(Integer, ForeignKey('horario.horario_id'))

class Cliente(Base):
    __tablename__ = 'cliente'
    cliente_id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellidos = Column(String(100), nullable=False)
    dni = Column(String(20), unique=True, nullable=False)
    email = Column(String(100))
    telefono = Column(String(20))

class Reserva(Base):
    __tablename__ = 'reserva'
    reserva_id = Column(Integer, primary_key=True)
    fecha_inicio = Column(Date, nullable=False)
    fecha_fin = Column(Date, nullable=False)
    apartamento_id = Column(Integer, ForeignKey('apartamento.apartamento_id'))
    cliente_id = Column(Integer, ForeignKey('cliente.cliente_id'))

class Pulsera(Base):
    __tablename__ = 'pulsera'
    pulsera_id = Column(Integer, primary_key=True)
    codigo_uid = Column(String(100), unique=True, nullable=False)
    tipo = Column(String(50))
    activa = Column(Boolean, default=True)

class Acceso(Base):
    __tablename__ = 'acceso'
    acceso_id = Column(Integer, primary_key=True)
    fecha_hora = Column(DateTime, nullable=False)
    tipo_acceso = Column(String(50))
    apartamento_id = Column(Integer, ForeignKey('apartamento.apartamento_id'))
    empleado_id = Column(Integer, ForeignKey('empleado.empleado_id'))
    pulsera_id = Column(Integer, ForeignKey('pulsera.pulsera_id'))

class EventoFichaje(Base):
    __tablename__ = 'evento_fichaje'
    evento_id = Column(Integer, primary_key=True)
    fecha_hora = Column(DateTime, nullable=False)
    tipo_evento = Column(String(50))
    empleado_id = Column(Integer, ForeignKey('empleado.empleado_id'))
