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
   #Load_json
    def load_from_json(self):
        try:
            with open("employees.json", "r", encoding="utf-8") as file:
                data = json.load(file) # stockena ao anaty data ilay zvt ao anatin'ilay fichier.Json
                self.employees=[

                ]
                for i in data:
                    employee = Employee(
                        i["id"],
                        i["nom"],
                        i["poste"],
                        i["salaire"]

                    )
                    self.employees.append(employee)
                print("Employés chargés avec succès.")
        except FileNotFoundError:
            print("le fichier n'existe pas")
        except Exception as e: 
            print("Error:",e) 
            
            #EXport_excel 
    def export_excel(self):
        try:
                

        # Créer un nouveau classeur Excel
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Employees"

        # En-têtes des colonnes
            sheet.append(["ID", "Nom", "Âge", "Salaire"])

        # Ajouter les données des employés
            for employee in self.employees:
                sheet.append([
                employee.emp_id,
                employee.name,
                employee.age,
                employee.salary
            ])

        except Exception as e:
            print("Error:",e)  



def menu ():
    manager = EmployeeManager()
    manager.load_from_json()
    

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
                id=int(input("id: "))
                nom=input("nom: ")
                poste=input("poste: ")
                salaire=float(input("salaire: "))

                employe = Employee(id, nom, poste, salaire)
                manager.add_employee(employe)
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
            
            print("Les employés ont été enregistrés dans employees.json.")
        except Exception as e:
            print("Error:", e)

      

       