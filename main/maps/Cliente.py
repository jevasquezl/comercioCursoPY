from marshmallow import Schema, fields, post_load, post_dump
from main.models import ClienteModel

class ClienteSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    email = fields.Email(required=True)
    telefono = fields.Str(required=True)
    rol = fields.Int(required=True)

    @post_load
    def make_cliente(self, data, **kwargs):
        return ClienteModel(**data)

    SKIP_VALUES = set(["fecha_registro"])    
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items()
            if key not in self.SKIP_VALUES
        }   
    