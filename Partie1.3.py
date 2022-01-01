class Rectangle:
    def __init__(self, lon=2, lar=3, nom="rectangle"):
       self.a = lon
       self.b = lar
       self.n=nom
#Afficher La largeur et la longeur et le nom du rectangle
    def afficher(self):
        print("la longeur du rectangle est :%d \nSa largeur est :%d \nSon nom est :%s" % (self.a, self.b, self.n))

#Calculer et afficher la surface
    def surface(self,rec):
        self.S=rec.a*rec.b #prendre les valeurs de la longeur et la largeur, et calculer la surface
        print("sa surface est : %d" % (self.S))
#Classe Carre qui herite du classe Rectangle
class Carre(Rectangle):
    print("\n")

"""Le programme principal"""
rec=Rectangle()
rec.afficher()
rec.surface(rec)
c=Carre(3,3,"carre")
print("Son nom:",c.n)
c.surface(c)
