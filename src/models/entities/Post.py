class Post():
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
    #diccionario    
    def to_JSON(self):
        return{
            'nombre':self.nombre,
            'descripcion':self.descripcion
        }