class Vecteur2D:
    """Constructeur pour initialiser les donnees"""
    def __init__(self, x=0, y=0):
       self.x = x
       self.y = y
       print("(%d, %d)" % (self.x, self.y))

"""Des objets du classe Vecteur 2D"""
print("Les coodonnees du 1er vecteur :")
v1=Vecteur2D()
print("Les coodonnees du 2eme vecteur :")
v2=Vecteur2D(2,5)
