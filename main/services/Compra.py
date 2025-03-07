from main.repositories import CompraRepository
from flask import request, jsonify
from main.auth.decorators import role_required
from main.maps import CompraSchema
from main.models import CompraModel
from main.maps import ClienteSchema
from main.maps import UsuarioSchema


compraRepository = CompraRepository()
compraSchema = CompraSchema()

class CompraService:

    @role_required([1,2])
    def get_compra(self, id):
        compra = compraRepository.get_one(id)
        return compraSchema.dump(compra, many=False)

    @role_required([1,2])
    def get_compras(self):
        # page = 1
        # per_page = 5

        # if request.get_json():
        #     filters = request.get_json().items()
        #     for key, value in filters:
        #         if key == 'page':
        #             page = int(value)
        #         elif key == 'per_page':
        #             per_page = int(value)

        compras = compraRepository.get_all()
        return compraSchema.dump(compras, many=True)
    
    def create_compra(self, data):
        compra = compraRepository.create(data)
        return compraSchema.dump(compra, many=False)
    
    def update_compra(self, id, data):
        compra = compraRepository.update(id, data)
        return compraSchema.dump(compra, many=False)
    
    def delete_compra(self, id):
        compra = compraRepository.delete(id)
        return compraSchema.dump(compra, many=False)
    
    def filter_compras(self, **kwargs):
        compras = compraRepository.filter(**kwargs)
        compras_json = [compra.to_json() for compra in compras]
        return compras_json
    
    def get_compras_by_cliente(self, cliente_id):
        compras = compraRepository.filter(cliente_id=cliente_id)
        compras_json = [compra.to_json() for compra in compras]
        return compras_json
    
    def get_compras_by_producto(self, producto_id):
        compras = compraRepository.filter(producto_id=producto_id)
        compras_json = [compra.to_json() for compra in compras]
        return compras_json
    
