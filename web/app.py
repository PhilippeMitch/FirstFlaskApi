"""
Registration of a user 0 tokens
Each user get 10 tokens
Store a sentence on our database for 1 token
Retreive his stord sentence on out database for 1 token
"""

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.SentenceDatabase
users = db["Users"]


def verifyPw(username, password):
    hashed_pw = users.find({
        "Username":username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode("utf8"), hashed_pw) == hashed_pw:
        return True
    else:
        return False

def countTokens(username):
    tokens = users.find({
        "Username":username

    })[0]["Tokens"]
    return tokens

class Register(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]

        hashed_pw = bcrypt.hashpw(password.encode("utf8"), bcrypt.gensalt())

        users.insert({
            "Username":username,
            "Password":hashed_pw,
            "Sentence":"",
            "Tokens":10
        })

        retJson = {
            "status":200,
            "msg":"You successfully signed for the API"
        }

        return jsonify(retJson)


class Store(Resource):
    def post(self):
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]
        sentence = postedData["sentence"]

        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status":302
            }
            return jsonify(retJson)

        num_tokens = countTokens(username)

        if num_tokens <= 0:
            retJson = {
                "status":301
            }
            return jsonify(retJson)
        
        users.update({
            "Username":username
        },
        {
            "$set":{
                "Sentence":sentence,
                "Tokens":num_tokens - 1
            }
        })

        retJson = {
            "status": 200,
            "msg":"Sentence saved successfully"
        }

        return jsonify(retJson)

class Get(Resource):
    def post(self):
        postedData = request.get_json()
        username = postedData["username"]
        password = postedData["password"]

        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status":302
            }
            return jsonify(retJson)

        num_tokens = countTokens(username)

        if num_tokens <= 0:
            retJson = {
                "status": 301
            }
            return jsonify(retJson)

        sentence = users.find({
            "Username":username
        })[0]["Sentence"]

        retJson = {
            "status":200,
            "msg": sentence
        }

        return jsonify(retJson)

api.add_resource(Register, '/register')
api.add_resource(Store, '/store')
api.add_resource(Get, '/get')



if __name__ =="__main__":
    app.run(host='0.0.0.0')

