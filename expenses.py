import csv
import os.path

class Expenses:
    def __init__(self, user):
        self.user = user

        if os.path.exists(f"{self.user}.csv"):
            pass
        else:
            with open(f"{self.user}.csv", 'a', newline = '') as csvfile:
                fieldnames = ['type', 'name', 'amount']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

        if os.path.exists(f"{self.user}_salary.csv"):
            pass
        else:
            with open(f"{self.user}_salary.csv", 'a', newline = '') as csvfile:
                fieldnames = ['salary']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

    @staticmethod
    def input_salary(user):
        salary = int(input("please type your salary: "))
        with open(f"{user}_salary.csv", 'w', newline = '') as csvfile:
            fieldnames = ['salary']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({'salary': salary})

    @staticmethod
    def input_expenses(user):
        type = input('please insert your expense type: ').lower()
        name = input('please type your expense name: ').lower()
        amount = int(input("please type your expense amount: "))

        with open(f"{user}.csv", 'a', newline = '') as csvfile:
                fieldnames = ['type', 'name', 'amount']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writerow({'type': type, 'name' : name, 'amount' : amount})
    
    @staticmethod
    def type_cost(user, type):
        expenses_total = 0

        with open(f"{user}.csv") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['type'] == type:
                    expenses_total += int(row['amount'])
        return expenses_total
        
    @staticmethod
    def calculate_percentage(user, type):
        category_total_cost = Expenses.type_cost(user, type)
        monthly_salary = 0
        with open(f"{user}_salary.csv") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    monthly_salary += int(row['salary'])
        print(f"Your monthly percentage spent in {type} is {(category_total_cost / monthly_salary) * 100}%")