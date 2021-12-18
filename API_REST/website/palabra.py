from flask import (
    make_response,
    abort
)
from config import db
from website.models import (
    Palabra,
    PalabraSchema
)

# Create a handler for our read (GET) palabras
def read_all():
    """
    This function responds to a request for /api/palabras
    with the complete lists of palabras

    :return:        sorted list of palabras
    """
    # Create the list of palabras from our data
    palabra = Palabra.query \
            .order_by(Palabra.id) \
            .all()
    
    #serialize the data for the response
    palabra_schema = PalabraSchema(many=True)

    return palabra_schema.dump(palabra).data


def read_one(palabra_id):
    """
    This function responds to a request for /api/people/{palabra_id}
    with one matching word from palabra

    :param palabra_id:   ID of word to find
    :return:            palabra matching ID
    """
    # Get the word requested
    palabra = Palabra.query \
        .filter(Palabra.id == palabra_id) \
        .one_or_none()

    # Did we find a Word?
    if palabra is not None:

        # Serialize the data for the response
        palabra_schema = PalabraSchema()
        return palabra_schema.dump(palabra).data

    # Otherwise, nope, didn't find that word
    else:
        abort(404, f'Word not found for Id: {palabra_id}')


def create(palabra):
    """
    This function creates a new word in the palabra structure
    based on the passed-in palabra data

    :param palabra:  word to create in palabra structure
    :return:        201 on success, 406 on word exists
    """
    param_palabra = palabra.get('palabra')
    param_significado = palabra.get('significado')

    existing_person = Palabra.query \
        .filter(Palabra.palabra == param_palabra) \
        .filter(Palabra.significado == param_significado) \
        .one_or_none()

    # Can we insert this word?
    if existing_person is None:

        # Create a person instance using the schema and the passed-in person
        schema = PalabraSchema()
        new_palabra = schema.load(palabra, session=db.session).data

        # Add the person to the database
        db.session.add(new_palabra)
        db.session.commit()

        # Serialize and return the newly created person in the response
        return schema.dump(new_palabra).data, 201

    # Otherwise, nope, person exists already
    else:
        abort(409, f'Palabra: {param_palabra} with significado: {param_significado} exists already')