from flask_restful import Resource
from main.maps import CompraSchema
from main.services import CompraService
from flask import request
from flask import jsonify

compraSchema = CompraSchema()
compraService = CompraService()

class CompraController(Resource):
    
    def get(self, id):
        compra = compraService.get_compra(id)
        return compra
    
    def delete(self, id):
        compra = compraService.delete_compra(id)
        return compra, 204
    
    def put(self, id):
        data = request.get_json()
        compra = compraService.update_compra(id, data)
        return compra, 201
    

class ComprasController(Resource):

    def get(self):
        compras =  compraService.get_compras()        
        return compras
    
    def post(self):
        data = compraSchema.load(request.get_json(), many=False)
        compra = compraService.create_compra(data)
        return compra, 201
                

    def get_by_cliente(self, cliente_id):
        compras = compraSchema.load(compraService.get_compras_by_cliente(cliente_id))
        return compraSchema.dump(compras, many=False)
    
    def get_by_producto(self, producto_id):
        compras = compraSchema.load(compraService.get_compras_by_producto(producto_id))
        return compraSchema.dump(compras, many=False)
