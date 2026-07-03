#ataovy ny devoir
class Employee:
    def __init__(self, id, nom, poste, salaire):
        self.id = id
        self.nom = nom
        self.poste = poste
        self.salaire = salaire

    def display_info(self):
        print(f"ID : {self.id}")
        print(f"Nom : {self.nom}")
        print(f"Poste : {self.poste}")
        print(f"Salaire : {self.salaire:,} Ar")

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "poste": self.poste,
            "salaire": self.salaire
        }



employe1 = Employee(1, "Jean", "Développeur", 1500000)

employe1.display_info()


print("\nDictionnaire :")
print(employe1.to_dict())