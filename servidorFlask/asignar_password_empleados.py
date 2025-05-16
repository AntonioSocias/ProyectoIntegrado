from flask import Flask
from werkzeug.security import generate_password_hash
from models import db, Empleado
import config

# Configurar la app para usar la base de datos
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Ejecutar en contexto de la app
with app.app_context():
    empleados_sin_password = Empleado.query.filter(Empleado.password == None).all()
    print(f"Se encontraron {len(empleados_sin_password)} empleados sin contraseña.")

    for empleado in empleados_sin_password:
        empleado.password = generate_password_hash("1234")  # puedes personalizarla si quieres
        print(f"Asignada contraseña a {empleado.nombre} {empleado.apellidos} (DNI: {empleado.dni})")

    db.session.commit()
    print("Contraseñas asignadas y guardadas correctamente.")
