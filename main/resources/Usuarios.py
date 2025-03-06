from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuarioModel
from main.auth.decorators import role_required
from flask_jwt_extended import get_jwt_identity

class Usuario(Resource):

    @role_required([1,2])
    def get(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        try:
            current_user = get_jwt_identity()

            if current_user['id'] == usuario.id or current_user['rol'] == 1:
                return usuario.to_json()
            else:
                return 'Unauthorized', 401

        except:
            return 'Resource not found', 404
    
    @role_required([1,2])
    def delete(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return '', 204

    @role_required([1,2])
    def put(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            if key == 'password':
                setattr(usuario, 'plain_password', value)
            else:
                setattr(usuario, key, value)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201

class Usuarios(Resource):

    @role_required([1,2])
    def get(self):
        try:
            page = 1
            per_page = 5
                   
            if request.get_json():
                filters = request.get_json().items()
                for key, value in filters:
                    if key == 'page':
                        page = int(value)
                    elif key == 'per_page':
                        per_page = int(value)

            usuarios = db.session.query(UsuarioModel)
            usuariosdic = []

            for result in usuarios:
                usuariosdic.append({"nombre" : result.nombre, "apellido" :result.apellido, "email" : result.email, "telefono" : result.telefono, "rol" : result.rol, "fecha_registro" : result.fecha_registro})
            
            usuariosdic = usuariosdic[(page-1)*per_page:page*per_page]

            return jsonify({
                'valid': True,
                'usuarios': [usuariosdic],
                'total': usuariosdic.__len__(),
                'pages': per_page,
                'page': page
            })
        except Exception as e:
            return str(e), 400
        
        
    @role_required([1,2])
    def post(self):
        usuario = UsuarioModel.from_json(request.get_json())
        usuario.rol = 2
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201