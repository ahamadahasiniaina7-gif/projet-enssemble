#ataovy ny devoir
import json
from openpyxl import Workbook


#atributs
class Employee:
    def __init__(self,id,nom,poste,salaire):
        self.id = id
        self.nom = nom
        self.poste = poste
        self.salaire = salaire
    
    #methode display_info
    def display_info(self):
        print(f"ID: {self.id}")
        print(f"NOM: {self.nom}")
        print(f"POSTE: {self.poste}")
        print(f"SALAIRE: {self.salaire}")

    def to_dict(self):
        return {
            "id" : {self.id},
            "nom" : {self.nom},
            "poste" : {self.poste},
            "salaire" : {self.salaire}
        }
        



class EmployeeManager:
    def __init__(self):
        self.employees = [] #tableau

    #methode ajouter employer
    def add_employee(self,employer):
        self.employees.append (employer)
        print("Employer ajouter avec succcess")

    #méthode trouver employer
    def find_employee(self,employer_id):
        for employer in self.employees:
            if employer.id == employer_id:
                return employer #misy valeur
        return None #vide
        

    #methode supprimer
    def remove_employee(self,employer_id):
        employer = self.find_employee(employer_id)
        if employer:
            self.employees.remove(employer) #.pop
            print(f"Employer supprimmer ave succcess {employer}")
        else:
            print("employer introuvable")    
            
            
        
    #display_all(afficher tout)
    def display_all(self):
        if not self.employees:
            print("aucun employer")
            return
        for employer in self.employees:
            employer.display_info()
    #crée une méthode
    import json




class Employee:
    def __init__(self, id, nom, poste, salaire):
        self.id = id
        self.nom = nom
        self.poste = poste
        self.salaire = salaire


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def save_to_json(self):
        data = []

        for emp in self.employees:
            data.append({
                "id": emp.id,
                "nom": emp.nom,
                "poste": emp.poste,
                "salaire": emp.salaire
            })

        with open("employees.json", "w", encoding="utf-8") as fichier:
            json.dump(data, fichier, indent=4, ensure_ascii=False)

        print("Les employés ont été enregistrés dans employees.json.")
        

class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["emp_id"],
            data["name"],
            data["age"],
            data["salary"]
        )




def menu ():
    manager = EmployeeManager()
    

    while True:
        print("""
            1:ajouter un employee
            2:afficher les employees
            3:supprimer un employee
            4:sauvegarder dans json
            5:charger json
            6:exporter vers exel
            0:quitter
              """)

        try:
            choix = int(input("entrer votre choix"))
            
            if choix ==1:
                #ajoiuter
            elif choix ==2:
                #afficher
            elif choix ==3:
                #supprimer
            elif choix ==4:
                #sauvegarde
            elif choix ==5:
                #charger
            elif choix ==6:
                #exporter
            elif choix ==0:
                #quitter
                print("au revoir")
            else:
                print("choix invalide")
        except ValueError:
            print("enter nomber valide")
            


        
        
