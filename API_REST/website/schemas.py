from marshmallow import fields
from website.ext import ma
from website.models import Palabra

class PalabraSchema(ma.SQLAlchemyAutoSchema): #Schema
    class Meta:
        model = Palabra
        load_instance = True