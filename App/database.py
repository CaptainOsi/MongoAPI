from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from settings import *

app = Flask(__name__)

app.config['MONGO_DBNAME'] = MONGO_BDDNAME
app.config['MONGO_URI'] = 'mongodb://' + MONGO_USER_NAME + ':' + MONGO_PASSWORD + '@' + MONGO_SERVER_NAME + ':' + MONGO_PORT + '/' + MONGO_BDDNAME

mongo = PyMongo(app)