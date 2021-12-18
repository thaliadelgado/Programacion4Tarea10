from flask import request, Blueprint
from flask_restful import Api, Resource

from .schemas import PalabraSchema
from .models import Palabra

palabra_v1_0_bp = Blueprint('palabra_v1_0_bp', __name__)

palabra_schema = PalabraSchema()

api = Api(palabra_v1_0_bp)

class PalabraListResource(Resource):
    def get(self):
        palabra = Palabra.get_all()
        result = palabra_schema.dump(palabra, many=True)
        return result
    
    def post(self,data):
        
        palabra_dict = data #palabra_schema.load(data)

        p = Palabra()

        p.palabra  = palabra_dict['palabra']
        p.significado=palabra_dict['significado']
        p.save()
        list = self.get()

        palabras = list#palabra_schema.dump(p)
        return palabras, 201

class PalabraResource(Resource):
    def get_palagra_by_id( self,palabra_id):
        p = Palabra.get_by_id(palabra_id)
        resp = palabra_schema.dump(p)
        return resp
    
    def delete(self):
        print(self)
        



api.add_resource(PalabraListResource, '/api/v1.0/palabras/', endpoint='palabra_list_resource')
api.add_resource(PalabraResource, '/api/v1.0/palabra/<int:palabra_id>', endpoint='palabra_resource')