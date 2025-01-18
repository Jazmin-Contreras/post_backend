from flask import Flask
from flask_cors import CORS
from routes.Post import main
from config import config
#importancion de rutas
from routes import Post
app=Flask(__name__)

def page_not_found(error):
    return "<h1>Pagina no encontrada<h1>"

if __name__=='__main__':
    app.config.from_object(config['development'])
    #asignacion de rutas
    app.register_blueprint(Post.main, url_prefix='/api/posts')
    #manejo de errores
    app.register_error_handler(404, page_not_found)
    app.run()
