from main import db
import datetime as dt

# #Estos modulos ya los trae flask por defecto, no hace falta instalarlos
from werkzeug.security import generate_password_hash, check_password_hash

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True, index=True)
    telefono = db.Column(db.Integer, nullable=False)
    fechaRegistro = db.Column(db.DateTime, default=dt.datetime.now(), nullable=False)
    rol = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', back_populates="cliente", uselist=False, single_parent=True)
    compra = db.relationship('Compra', back_populates="cliente", cascade="all, delete-orphan")


    def __repr__(self):
        return f'{self.nombre}'

    def to_json(self):
        Cliente_json = {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'rol': self.rol,
            'fechaRegistro': str(self.fechaRegistro)
        }
        return Cliente_json

    #cuando yo retorne el objeto Cliente para guardar en mi db, voy a utilizar el atributo plain_password, el setter, para generar el hash de la contraseña
    @staticmethod
    def from_json(Cliente_json):
        id = Cliente_json.get('id')
        nombre = Cliente_json.get('nombre')
        email = Cliente_json.get('email')
        telefono = Cliente_json.get('telefono')
        fechaRegistro = Cliente_json.get('fechaRegistro')
        rol = Cliente_json.get('rol')
        return Cliente(
            id = id,
            nombre = nombre,
            email = email,
            telefono = telefono,
            rol = rol,
            fechaRegistro = fechaRegistro
        )
        