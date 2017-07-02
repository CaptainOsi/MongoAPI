from App.database import *


def getAllUser():
    user = mongo.db.user
    output = []
    for q in user.find():
        output.append({'firstname': q['firstname'], 'lastname': q['lastname'], 'login': q['login']})

    return jsonify({'result': output})


def get_one_user(login):
    user = mongo.db.user
    q = user.find_one({'login': login})
    if q:
        output = {'firstname': q['firstname'], 'lastname': q['lastname'], 'login': q['login']}
    else:
        output = 'No results found'
    return jsonify({'result': output})


def add_one_user(firstname, lastname, login, password):
    user = mongo.db.user
    output = 'Datas should be filled'

    if  (login == None) or (password == None) or (firstname == None) or (lastname == None):
        return jsonify({'result': output})

    user_id = user.insert({'firstname': firstname, 'lastname': lastname, 'login': login, 'password': password})
    new_user = user.find_one({'_id': user_id})

    output = {'firstname': new_user['firstname'], 'lastname': new_user['lastname'], 'login': new_user['login']}

    return jsonify({'result': output})
