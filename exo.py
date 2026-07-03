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
        




"""#exercice 2
class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee} ajouté.")

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee} supprimé.")
        else:
            print("Employé non trouvé.")

    def find_employee(self, employee):
        if employee in self.employees:
            print(f"{employee} trouvé.")
            return True
        else:
            print(f"{employee} non trouvé.")
            return False

    def display_all(self):
        if not self.employees:
            print("Aucun employé.")
        else:
            print("Liste des employés :")
            for employee in self.employees:
                print(employee)



manager = EmployeeManager()

manager.add_employee("Alice")
manager.add_employee("Bob")

manager.display_all()

manager.find_employee("Alice")

manager.remove_employee("Bob")

manager.display_all()

#exercice 3
import json

class EmployeeManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        self.employees = [
            emp for emp in self.employees
            if emp["id"] != employee_id
        ]

    def find_employee(self, employee_id):
        for emp in self.employees:
            if emp["id"] == employee_id:
                return emp
        return None

    def display_all(self):
        for emp in self.employees:
            print(emp)

    def save_to_json(self):
        with open("employees.json", "w", encoding="utf-8") as file:
            json.dump(self.employees, file, ensure_ascii=False, indent=4)"""