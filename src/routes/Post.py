from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from models.entities.Post import Post
from models.PostModel import PostModel
main=Blueprint('post_blueprint',__name__)
@main.route('/')
@cross_origin()
def get_posts():
    try:
        posts=PostModel.get_posts()
        return jsonify(posts)
    except Exception as ex: 
        return jsonify({'message':str(ex)}),500
@main.route('/<nombre>')
@cross_origin()
def get_post(nombre):
    try:
        post=PostModel.get_post(nombre)
        if post!=None:
            return jsonify(post)
        else:
            return jsonify({}),404
    except Exception as ex: 
        return jsonify({'message':str(ex)}),500
    
@main.route('/add', methods=['POST'])
@cross_origin()
def add_post():
    try:
        nombre=request.json.get('nombre')
        descripcion=request.json.get('descripcion')
        nuevo_post = Post(nombre, descripcion)
        a_rows = PostModel.add_post(nuevo_post)
        if a_rows == 1:
            return jsonify({
                'message': 'Post agregado exitosamente',
                'post': {
                    'nombre': nuevo_post.nombre,
                    'descripcion': nuevo_post.descripcion
                }
            }), 201
        else:
            return jsonify({'message': 'No se pudo guardar el post'}), 500
            
    except Exception as ex:
        print(f"Error general: {str(ex)}") 
        return jsonify({'message': f'Error del servidor: {str(ex)}'}), 500
    
@main.route('/delete/<string:nombre>', methods=['DELETE'])
@cross_origin()
def delete_post(nombre):
    try:
        affected_rows = PostModel.delete_post(nombre)
        
        if affected_rows == 1:
            return jsonify({
                'message': f'Post "{nombre}" eliminado exitosamente'
            }), 200
        else:
            return jsonify({
                'message': f'No se encontró un post con el nombre "{nombre}"'
            }), 404
        
    except Exception as ex:
        print(f"Error al eliminar: {str(ex)}")  
        return jsonify({'message': f"Error al eliminar: {str(ex)}"}), 500
    
    
