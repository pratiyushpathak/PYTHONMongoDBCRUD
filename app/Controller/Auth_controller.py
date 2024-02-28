
from MongoBankingProject.app.Controller.Card_Controller import cardcontroller

try:
    def userAuthentication(collection, email):


        while True:
            print('Your Email is: ', email)
            password = input('Enter your password: ')

            user = collection.find_one({'email': email, 'password': password})

            if user:
                print('User successfully Authenticated')
                cardType = user.get('cardType')
                id = user.get('c_id')
                match cardType:
                    case 'silver':
                        cardcontroller(1,id,collection)
                    case 'gold':
                        cardcontroller(2,id,collection)
                break
            else:
                print('Please Try again')

except Exception as e:
    print('An error occurred:', e)