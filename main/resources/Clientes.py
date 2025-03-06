from flask_restful import Resource
from flask import jsonify, request
from .. import db
from main.models import ClienteModel
from main.auth.decorators import role_required
from flask_jwt_extended import get_jwt_identity

class Cliente(Resource):
    
    @role_required([1,2])
    def get(self, id):
        cliente = db.session.query(ClienteModel).get_or_404(id)
        # cliente = db.session.query(ClienteModel).filter(ClienteModel.id == id).first()
        try:
            return cliente.to_json()
        except:
            return 'Resource not found', 4

    @role_required([1,2])
    def delete(self, id):
        cliente = db.session.query(ClienteModel).get_or_404(id)
        current_user = get_jwt_identity()
        if current_user['rol'] >= 1:
            try:
                db.session.delete(cliente)
                db.session.commit()
                return '', 204
            except:
                return '', 404
        else:
            return 'Unauthorized', 401

    @role_required([1,2])
    def put(self, id):
        cliente = db.session.query(ClienteModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(cliente, key, value)
        try:
            db.session.add(cliente)
            db.session.commit()
            return cliente.to_json(), 201
        except:
            return '', 404
        
    # @role_required([1,2])
    # def put(self, id):
    #     usuario = db.session.query(UsuarioModel).get_or_404(id)
    #     data = request.get_json().items()
    #     for key, value in data:
    #         if key == 'password':
    #             setattr(usuario, 'plain_password', value)
    #         else:
    #             setattr(usuario, key, value)
    #     db.session.add(usuario)
    #     db.session.commit()
    #     return usuario.to_json(), 201

class Clientes(Resource):
    
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
                
            clientes = db.session.query(ClienteModel)
            # clientes = db.session.query(UsuarioModel).filter(UsuarioModel.role == 'Cliente')
            clientesdic = []

            for result in clientes:
                clientesdic.append({"nombre" : result.nombre, "email" : result.email, "telefono" : result.telefono, "fechaRegistro" : result.fechaRegistro, "rol" : result.rol})

            clientesdic = clientesdic[(page-1)*per_page:page*per_page]

            return jsonify({
                'valid': True,
                'usuarios': [clientesdic],
                'total': clientesdic.__len__(),
                'pages': per_page,
                'page': page
            })
                    
        except Exception as e:
            return str(e), 400
        
    @role_required([1,2])
    def post(self):
        cliente = ClienteModel.from_json(request.get_json())
        data = db.session.query(ClienteModel).filter(ClienteModel.email == cliente.email).first()
        if data:
            return 'Email already exists', 400
        else:
            db.session.add(cliente)
            db.session.commit()
        
        return cliente.to_json(), 201
