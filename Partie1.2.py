class Vecteur2D:
    def __init__(self, x=0, y=0):
       self.x = x
       self.y = y

#Méthde pour afficher les coordonnees des deux vecteurs
    def afficher(self):
        print("(%d, %d)" % (self.x, self.y))

#Méthode pour calculer et afficher la somme des deux vecteurs
    def somme(self,v1,v2):
        self.X=v1.x+v2.x #prend les valeurs des x des deux vecteurs et calculer leur somme
        self.Y=v1.y+v2.y #prend les valeurs des y des deux vecteurs et calculer leur somme
        print("La somme des deux vecteurs est : \nv=(%d, %d)" % (self.X, self.Y))
"""Le programme principal"""
v1, v2, v=Vecteur2D() ,Vecteur2D(2,6),Vecteur2D()

print("Les coordonnees du vecteur 1 :")
v1.afficher()
print("Les coordonnees du vecteur 2 :")
v2.afficher()
v.somme(v1,v2)