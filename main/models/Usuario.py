from main import db
import datetime as dt

# #Estos modulos ya los trae flask por defecto, no hace falta instalarlos
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(60), nullable=False, unique=True, index=True)
    rol = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    role = db.relationship('Role', back_populates="usuario", uselist=False, single_parent=True)
    
    telefono = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    fecha_registro = db.Column(db.DateTime, default=dt.datetime.now(), nullable=False)
    compra = db.relationship('Compra', back_populates="usuario", cascade="all, delete-orphan")

    #Getter de la contraseña, la contraseña plana no puedo leerla, es decir no puedo acceder a ella, es una propiedad de la clase pero no va a estar en la base de datos, yo en esta clase voy a tener un atributo plain_password, pero nunca se va a guardar en mi db, solo lo voy a usar para generar el hash
    @property
    def plain_password(self):
        raise AttributeError('Password can\'t be read')

    #setter de la contraseña, toma un valor en texto plano
    #genera el hash y lo guarda en el atributo password
    @plain_password.setter
    def plain_password(self, password):
        self.password = generate_password_hash(password)
    
    #metodo que compara una contraseña en texto plano generando su hash y comparandolo con el hash guardado en mi base de datos
    def validate_pass(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'{self.nombre}'

    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'rol': self.rol,
            'fecha': str(self.fecha_registro)
        }
        return usuario_json

    #cuando yo retorne el objeto usuario para guardar en mi db, voy a utilizar el atributo plain_password, el setter, para generar el hash de la contraseña
    @staticmethod
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        email = usuario_json.get('email')
        telefono = usuario_json.get('telefono')
        password = usuario_json.get('password')
        rol = usuario_json.get('rol')
        fecha_registro = usuario_json.get('fecha_registro')
        return Usuario(
            id = id,
            nombre = nombre,
            apellido = apellido,
            email = email,
            telefono = telefono,
            plain_password = password,
            rol = rol,
            fecha_registro = fecha_registro
        )
        