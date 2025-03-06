from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ProductoModel
from main.auth.decorators import role_required

class Producto(Resource):
    def get(self, id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        try:
            return producto.to_json()
        except:
            return 'Resource not found', 404

    @role_required([1])
    def put(self, id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(producto, key, value)
        try:
            db.session.add(producto)
            db.session.commit()
            return producto.to_json(), 201
        except:
            return '', 404

    @role_required([1])
    def delete(self, id):
        producto = db.session.query(ProductoModel).get_or_404(id)
        try:
            db.session.delete(producto)
            db.session.commit()
        except:
            return '', 404


class Productos(Resource):

    @role_required([1])
    def get(self):
        page = 1
        per_page = 5

        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)
            
        productos = db.session.query(ProductoModel)
        productosdic = []

        for result in productos:
            productosdic.append({"nombre" : result.nombre, "precio" :result.precio, "imagen" : result.imagen, "descripcion" : result.descripcion, "stock" : result.stock})

        productosdic = productosdic[(page-1)*per_page:page*per_page]

        return jsonify({
            'productos': [productosdic],
            'total': usuariosdic.__len__(),
            'pages': per_page,
            'page': page
        })

    @role_required([1])
    def post(self):
        producto = ProductoModel.from_json(request.get_json())
        db.session.add(producto)
        db.session.commit()
        return producto.to_json(), 201