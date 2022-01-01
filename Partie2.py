class etudiant:
    def _init_(self, nom, prenom, age, cne, moyenne):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.cne = cne
        self.moyenne = moyenne

# list de type etudiant
etudiant = [
    {'nom': 'Izougaghen', 'prenom': 'Mouna', 'age': 19, 'cne': 222223, 'moyenne':19},
    {'nom': 'El harti', 'prenom': 'imane', 'age': 20, 'cne': 389923, 'moyenne': 20},
]

# trie par age
print("\tListe triee par age :")
etudiant.sort(key=lambda x: x.get('age'))
print(etudiant)
# trie par moyenne
print("\n\tListe triee par moyenne :")
etudiant.sort(key=lambda x: x.get('moyenne'))
print(etudiant)