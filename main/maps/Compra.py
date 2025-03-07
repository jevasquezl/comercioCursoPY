from marshmallow import Schema, fields, post_load, post_dump
from main.models import CompraModel

class CompraSchema(Schema):
    id = fields.Int(dump_only=True)
    fecha_compra = fields.DateTime(required=True)
    usuarioId = fields.Int(required=True)
    usuario = fields.Nested('UsuarioSchema', only=['id', 'nombre', 'apellido', 'email', 'rol'])
    clienteId = fields.Int(required=True)
    cliente = fields.Nested('ClienteSchema', only=['id', 'nombre', 'email', 'telefono', 'rol'])


    @post_load
    def make_compra(self, data, **kwargs):
        return CompraModel(**data)

    SKIP_VALUES = set([""])    
    @post_dump
    def remove_skip_values(self, data, **kwargs):
        return {
            key: value for key, value in data.items()
            if key not in self.SKIP_VALUES
        }
    