from Controller.Auth_controller import userAuthentication
from MongoBankingProject.app.Config.ConnectDatabase import formCollection
from services.CreateUser import createuser
collection = formCollection()

email = input('Enter Your Email: ')

if collection.find_one({'email': email}):
    userAuthentication(collection, email)

else:
    createuser(collection, email)