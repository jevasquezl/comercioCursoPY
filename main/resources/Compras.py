from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import CompraModel
from main.auth.decorators import role_required
from flask_jwt_extended import get_jwt_identity

class Compra(Resource):

    @role_required([1,2])
    def get(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        current_user = get_jwt_identity()
        if current_user['usuarioId'] == compra.usuarioId or current_user['role'] == 'admin':
            try:
                return compra.to_json()
            except:
                return '', 404
        else:
            return 'Unauthorized', 401

    @role_required([1,2])
    def put(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        current_user = get_jwt_identity()
        if current_user['usuarioId'] == compra.usuarioId or current_user['role'] == 'admin':
            data = request.get_json().items()
            for key, value in data:
                setattr(compra, key, value)
            try:
                db.session.add(compra)
                db.session.commit()
                return compra.to_json(), 201
            except:
                return '', 404
        else:
            return 'Unauthorized', 401            

    @role_required([1,2])
    def delete(self, id):
        compra = db.session.query(CompraModel).get_or_404(id)
        current_user = get_jwt_identity()
        if current_user['usuarioId'] == compra.usuarioId or current_user['role'] == 'admin':
            try:
                db.session.delete(compra)
                db.session.commit()
                return '', 204
            except:
                return '', 404
        else:
            return 'Unauthorized', 401    

class Compras(Resource):

    @role_required([1,2])
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
        compras = db.session.query(CompraModel)
        comprasdic = []

        for result in compras:
            comprasdic.append({"fecha_compra" : result.fecha_compra, "usuarioId" : result.usuarioId, "clienteId" : result.clienteId})
                              
        comprasdic = comprasdic[(page-1)*per_page:page*per_page]
    
        return jsonify({
            'valid': True,
            'compras': [comprasdic],
            'total': comprasdic.__len__(),
            'pages': per_page,
            'page': page
        })
        


    @role_required([1,2])    
    def post(self):
        compra = CompraModel.from_json(request.get_json())
        db.session.add(compra)
        db.session.commit()
        return compra.to_json(), 201