from pymongo import MongoClient
import bcrypt


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.Users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        self.Users.insert({'username': data.username, 'name': data.name, 'email': data.email, 'password': hashed})

        # myuser = self.Users.find_one({'username': data.username})
        # if bcrypt.checkpw('test123'.encode(), myuser['password']):
        #     print("this matches")
