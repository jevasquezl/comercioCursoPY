from main import db
import datetime as dt

# #Estos modulos ya los trae flask por defecto, no hace falta instalarlos
from werkzeug.security import generate_password_hash, check_password_hash

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    usuario = db.relationship('Usuario', back_populates="role", uselist=False, single_parent=True)
    cliente = db.relationship('Cliente', back_populates="role", uselist=False, single_parent=True)


    # compras = db.relationship('Compra', back_populates="Roles", cascade="all, delete-orphan")
    