from .. import db
from main.models import CompraModel

class CompraRepository:
    __modelo = CompraModel

    @property
    def modelo(self):
        return self.__modelo
    
    def get_all(self):
        return db.session.query(self.modelo).all()
                   
    def get_one(self, id):
        return db.session.query(self.modelo).get_or_404(id)
    
    def create(self, data):
        try:
            db.session.add(data)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return data
    
    def update(self, id, data):
        compra = db.session.query(self.modelo).get_or_404(id)  
        try:
            for key, value in data.items():
                setattr(compra, key, value)
            db.session.add(compra)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409

        db.session.add(compra)
        db.session.commit()
        return compra    
        
    def delete(self, id):
        compra = db.session.query(self.modelo).get_or_404(id)
        try:
            db.session.delete(compra)
            db.session.commit()
        except Exception as error:
            db.session.rollback()
            return str(error), 409
        return ''
    
    def filter(self, **kwargs):
        return db.session.query(self.modelo).filter_by(**kwargs).all()
    

    
