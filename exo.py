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
        




    







        
        
