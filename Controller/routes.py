from Model.frameworkModel import *
from Model.userModel import *
from flask_restful import Resource, Api, reqparse
import urlparse

@app.route('/user', methods=['GET'])
def get_all_users():
    return getAllUser()

@app.route('/user',methods=['POST'])
def add_user():
    parser = reqparse.RequestParser()
    parser.add_argument('login')
    parser.add_argument('password')
    parser.add_argument('firstname')
    parser.add_argument('lastname')
    args = parser.parse_args()
    login = args['login']
    password = args['password']
    firstname = args['firstname']
    lastname = args['lastname']

    return add_one_user(firstname,lastname,login,password)

@app.route('/user/<login>', methods=['GET'])
def get_user(login):
    return get_one_user(login)