import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource
from main.models import UsuarioModel
import json


# pip install pysqlite3

# import sqlite3 as sql
 
# conn = sql.connect('test_database.db')
 
# cursor = conn.cursor()
 
# cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS cars(
#                     car_id INTEGER PRIMARY KEY,
#                     brand TEXT NOT NULL,
#                     price INTEGER NOT NULL
#                 )''')
 
# cursor.execute("INSERT INTO cars (brand, price) VALUES ('TATA', 300000)")
# cursor.execute("INSERT INTO cars (brand, price) VALUES ('Mahindra', 2500000)")
 
# cursor.execute("SELECT * FROM cars")
# print("Selection successfull...")
 
# data = cursor.fetchall()
# for values in data:
#     print(values)

# conn.commit()
 
# cursor.close()
# conn.close()


# load_dotenv() # will search for .env file in local folder and load variables

# server = os.getenv("server")
# database = os.getenv("database")
# name = os.getenv("name")
# password = os.getenv("password")
# DB_NAME = 'mssql+pyodbc://'+name+':'+password+'@'+server+'/'+database+'?driver=ODBC Driver 17 for SQL Server'




# app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PATH}{DB_NAME}'
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_NAME
# app.config['SQLALCHEMY_ECHO'] = True

# db = SQLAlchemy(app)
# db.init_app(app)

# class Usuario(): 

#     def getDato(self, id):
#         usuario = db.session.query(UsuarioModel).filter(UsuarioModel.id == id).first()           
#         return [usuario]

#     def getDatos(self):
#         usuarios = db.session.query(UsuarioModel).all()            
#         return usuarios


# cursor = conn.cursor()

# cursor.execute("SELECT * FROM cars")
# print("Selection successfull...")

# columns = [col[0] for col in usuarios]
# data = [dict(zip(columns, row)) for row in rows]

# to_json = json.dumps(data, indent=2)
# print(to_json)

        # usuariosdic = []

# for result in usuarios:
#     usuariosdic.append({"nombre" : result.nombre, "apellido" :result.apellido})



# _usuario = Usuario() # Singleton

# # usuario = usuario.getDato(2)

# usuarios = _usuario.getDatos()
# # columns = [col for col in usuarios]
# # data = [dict(zip(columns, row)) for row in usuarios]
# # to_json = json.dumps(data, indent=2)
# # print(to_json)

# usuariosdic = []

# for result in usuarios:
#     usuariosdic.append({"nombre" : result.nombre, "apellido" :result.apellido})
# Tojson = json.dumps(usuariosdic, indent=2)


# print(usuariosdic)
# print(Tojson)

# columns = [col[0] for col in usuarios]
# data = [dict(zip(columns, row)) for row in rows]

# to_json = json.dumps(data, indent=2)
# print(to_json)


# print(usuariosdic)

#     i = i + 1

# # Create a list of dictionaries
# my_dict = [{'course':'python','fee':4000}, {'duration':'60days', 'discount':1200}]
# print("Original list:\n",my_dict)

# # Convert list of dictionaries to JSON
# jsondict = json.dumps(my_dict)
# print("Convert list of dictionaries to JSON:\n",jsondict)


# def decorador(func):
#     def wrapper(*args, **kwargs):
#         print("Antes de la función")
#         func(*args, **kwargs)
#         print("Después de la función")
#     return wrapper

def conPeriso(roles):
    def decorador(func):
        def wrapper(*args, **kwargs):
            if nombre['role'] in roles:
                return func(*args, **kwargs)
            else:
                print(f"No tienes permisos {nombre['nombres']}")
        return wrapper
    return decorador

nombre = {
    'nombres': 'Juan',
    'role': 'Cliente'
}

@conPeriso(['Admin','Cliente'])
def saludar(nombre):
    print(f"Hola mundo {nombre['nombres']}")


saludar(nombre)