from MongoBankingProject.app.services.Deposit import deposit
from MongoBankingProject.app.services.Withdraw import withdraw
from MongoBankingProject.app.services.Display import display
from MongoBankingProject.app.services.IncreaseLimit import increaselimit

def view(id, collection):
    display(id, collection)

def withdrawmoney(id, collection):
    user = collection.find_one({'c_id': id})
    limit = user.get('limit')
    print('Your Card Limit is: ',limit)
    if limit != 0:
        amount = int(input('Please Enter the amount to withdraw: '))
        if amount<=limit:
            withdraw(amount, id, collection)
        else:
            print('Amount more than limit cannot be withdrawn')


def depositmoney(id, collection):
    user = collection.find_one({'c_id': id})
    loan = user.get('loan')
    limit = user.get('limit')

    print('Your Card Loan is: ', loan)
    if loan != 0:
        amount = int(input('Please Enter the amount to deposit: '))
        if amount <= loan:
            deposit(amount, id, collection)
        else:
            print('Amount more than limit cannot be deposited')

def increaseLimit(id, collection):
    user = collection.find_one({'c_id': id})
    cardType = user.get('cardType')
    if cardType == 'silver':
        print('Not Valid for silver card users')
    else:
        if (user.get('loan') + user.get('limit')) <= 100000:
            increaselimit(id, collection)
        else:
            print('Limit can only be exceeded once for a user')
