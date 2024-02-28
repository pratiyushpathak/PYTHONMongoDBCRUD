from MongoBankingProject.app.Controller.FunctionsController import view
from MongoBankingProject.app.Controller.FunctionsController import withdrawmoney
from MongoBankingProject.app.Controller.FunctionsController import depositmoney
from MongoBankingProject.app.Controller.FunctionsController import increaseLimit


def subMenu():
    print('1. View')
    print('2. Withdraw')
    print('3. Deposit')
    print('4. Increase Limit')
    print('5. Exit')

def cardcontroller(num, id, collection):
    user = collection.find_one({'c_id': id})
    fname = user.get('firstName')
    flag = False

    while not flag:
        print(f"*********{'SILVER' if num == 1 else 'GOLD'}**********")
        print('Hello',fname.upper())
        subMenu()
        options = int(input('Enter your choice: '))

        match options:
            case 1:
                view(id, collection)
            case 2:
                withdrawmoney(id, collection)
            case 3:
                depositmoney(id, collection)
            case 4:
                increaseLimit(id, collection)
            case 5:
                flag = True
            case _:
                print('Enter a valid choice')