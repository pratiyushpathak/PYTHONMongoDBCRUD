import random

from MongoBankingProject.app.Controller.Auth_controller import userAuthentication
def createuser(collection, email):
    rand = random.Random()
    count = int(rand.random() * 10000)
    c_id = count+1
    firstName = input('Enter First Name: ')
    lastName = input('Enter Last Name: ')
    print('Email: ', email)
    password = input('Enter password: ')
    loan = 0
    cardType = input('Enter Card Type [silver / gold]: ')
    limit = 50000 if cardType == 'silver' else 100000

    user = {
        'c_id': c_id,
        'firstName': firstName,
        'lastName': lastName,
        'email': email,
        'password': password,
        'loan': loan,
        'cardType': cardType,
        'limit': limit
    }

    result = collection.insert_one(user)

    if result.inserted_id:
        print("User created successfully with ID:", result.inserted_id)
        userAuthentication(collection, email)
    else:
        print("Failed to create user")
