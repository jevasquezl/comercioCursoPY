from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps
from .. import jwt



def role_required(roles):
    def wrapper(function):
        @wraps(function)
        def decorator(*args, **kwargs):
            try:
                #Verificar que el JWT es correcto
                verify_jwt_in_request()
                #Obtenemos los claims (peticiones), que estan dentro del JWT
                claims = get_jwt()
                if claims['rol'] in roles:
                    return function(*args, **kwargs)
                else:
                    return 'Rol not allowed', 403
            except KeyError as e:
                return 'Token not valid', 401

        return decorator
    return wrapper 


#decoradores que ya trae el jwt, pero los modificamos, redeifimos


@jwt.user_identity_loader
def user_identity_lookup(usuario):
    
    return {
        'id': usuario.id,
        'rol': usuario.rol
    }


@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    claims = {
        'id': usuario.id,
        'rol': usuario.rol,
        'email': usuario.email
    }
    return claims

