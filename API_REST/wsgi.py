from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run()

# WSGI : crearemos un archivo que servirá como punto de entrada para nuestra aplicación. 
# Esto indicará a nuestro servidor de Gunicorn cómo interactuar con la aplicación.

# Luego por terminal
# se corre el siguiente comando "gunicorn --bind 0.0.0.0:5000 wsgi:app" para levantar la app