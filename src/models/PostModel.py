from database.db import get_connection
from models.entities.Post import Post

class PostModel():
    @classmethod
    def get_posts(self):
        try:
            connection=get_connection()
            posts=[]
            #cursor
            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre, descripcion FROM post ORDER BY nombre ASC")
                resultset=cursor.fetchall()
                
                for row in resultset:
                    post=Post(row[0],row[1])
                    posts.append(post.to_JSON())

            connection.close()
            return posts
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_post(self, nombre):
        try:
            connection=get_connection()
            #cursor
            with connection.cursor() as cursor:
                cursor.execute("SELECT nombre, descripcion FROM post WHERE nombre = %s",(nombre,))
                row=cursor.fetchone()
                post=None
                if row != None:
                    post=Post(row[0],row[1])
                    post=post.to_JSON()
            connection.close()
            return post
        except Exception as ex:
            raise Exception(ex)      
    
    @classmethod
    def add_post(cls, post):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("INSERT INTO post (nombre, descripcion) VALUES (%s, %s)", (post.nombre, post.descripcion))
                affected_rows = cursor.rowcount
                connection.commit()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        finally:
            if connection:
                connection.close()
    
    @classmethod
    def delete_post(cls, nombre):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM post WHERE nombre = %s", (nombre,))
                affected_rows = cursor.rowcount
                connection.commit()
                return affected_rows
        except Exception as ex:
            raise Exception(ex)
        finally:
            if connection:
                connection.close()