from marshmallow import Schema, fields, post_load, post_dump
from main.models import UsuarioModel

class UsuarioSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(load_only=True)
    rol = fields.Int(required=True)
    fecha_registro = fields.DateTime(dump_only=True)
    
    @post_load
    def make_usuario(self, data, **kwargs):
        return UsuarioModel(**data)

    SKIP_VALUES = set(["password", "fecha_registro"])    
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items()
            if key not in self.SKIP_VALUES
        }
    
    
