from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_restful import abort
import redis
import json
import requests
from website.resources import PalabraListResource,PalabraResource
from website.models import Palabra

pl = PalabraListResource()
pr = PalabraResource()

# Se establese la conexión de redis en la base de datos 0
# redis://localhost:6379
collection = redis.Redis(host='localhost', port=6379, db=0)
hashName = "diccionario"


views = Blueprint('views', __name__)



@views.route('/palabra_list_resource',methods=['GET'])
def get_palabras():
    palabras= pl.get()
    return jsonify(palabras)



@views.route('/', methods=['GET', 'POST'])
def home():     
    list = pl.get()
    return render_template("home.html", palabras = list)



@views.route('/delete-palabra/<int:palabra_id>', methods=['POST'])
def delete_note():
    palabra_id = request.args.get('id')
    print(palabra_id)

    return redirect('/')



@views.route('/editar', methods=['GET'])
def editar():    
    palabra_id = request.args.get('id')
    model = pr.get_palagra_by_id(palabra_id=palabra_id)
 
    return render_template("editar.html", model = model)



@views.route('/ver-palabra', methods=['GET'])
def ver_palabra():    
    
    palabra_id = request.args.get('id')
    model = pr.get_palagra_by_id(palabra_id=palabra_id)

    return render_template("ver.html", model = model)



@views.route('/agregar', methods=['GET'])
def agregar():    
    return render_template("agregar.html")

@views.route('/agregarPalabra', methods=['POST'])
def agregar_palabra():
    
    palabra = request.form.get('palabra')
    significado = request.form.get('significado')
    data = {
        'palabra':palabra,
        'significado':significado
    }
    pl.post(data)

    return redirect('/')


