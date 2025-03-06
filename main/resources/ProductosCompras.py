from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductoCompraModel
from main.auth.decorators import role_required

class ProductosCompras(Resource):

    @role_required([1,2])
    def get(self):

        productoscompras = db.session.query(ProductoCompraModel)

        productoscomprasdic = []

        for result in productoscompras:
            productoscomprasdic.append({"productoId" : result.productoId, "compraId" :result.compraId})

        productoscomprasdic = productoscomprasdic[(page-1)*per_page:page*per_page]
        return jsonify({
            'productoscompras': [productoscomprasdic]
        })

    @role_required([1,2])
    def post(self):
        productocompra = ProductoCompraModel.from_json(request.get_json())
        db.session.add(productocompra)
        db.session.commit()
        return productocompra.to_json(), 201

class ProductoCompra(Resource):

    @role_required([1,2])
    def get(self, id):
        productocompra = db.session.query(ProductoCompraModel).get_or_404(id)
        try:
            return productocompra.to_json()
        except:
            return '', 404

    @role_required([1,2])
    def delete(self, id):
        productocompra = db.session.query(ProductoCompraModel).get_or_404(id)
        try:
            db.session.delete(productocompra)
            db.session.commit()
            return '', 204
        except:
            return '', 404
    
    @role_required([1,2])
    def put(self, id):
        productocompra = db.session.query(ProductoCompraModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(productocompra, key, value)
        try:
            db.session.add(productocompra)
            db.session.commit()
            return productocompra.to_json(), 201
        except:
            return '', 404