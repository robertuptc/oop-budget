# # After you write all your classes, use this file to call them all together and run your program
from expenses import Expenses

menu = """What would you like to do?
Options:
1. Create new user
2. Add new expense
3. Display category total expense
4. Enter Monthly Salary
5. Percentage of income spent on category type
6. Quit

: """

user = input("Please input your username: ").lower()
print('')
mode = input(menu)

while mode != '6':
    if mode == "1":
        new_user = input("What is your username: ").lower()
        new_user = Expenses(new_user)
        mode = input(menu)
    elif mode == "2":
        Expenses.input_expenses(user)
        print('')
        mode = input(menu)
    elif mode == '3':
        type = input('please enter the category of the expense to be calculated: ').lower()
        total = Expenses.type_cost(user, type)
        print(f"Your total {type} expense is ${total}.")
        print('')
        mode = input(menu)
    elif mode == '4':
        Expenses.input_salary(user)
        print('')
        mode = input(menu)
    elif mode == '5':
        type = input('please enter the category of the expense to be calculated: ').lower()
        Expenses.calculate_percentage(user, type)
        print('')
        mode = input(menu)
    else:
        pass
