from app import app
from flask import request
from app import db
from stuff import Stuff


@app.route('/')
def index():
    firstmember = Stuff.query.first()
    return '<h1> Here you can find stuff list! </h1>'


@app.route('/stuff')
def view():
    stuff = Stuff.query.first()
    if stuff is not None:
        return str('First member name \n' + stuff.__str__())
    else:
        return "Stuff with this id does not exist"


@app.route('/stuff/<id>')
def get_stuff(id):
    stuff = Stuff.query.get(id)
    if stuff is not None:
        return stuff.__str__()
    else:
        return "Stuff with this id does not exist"


@app.route('/stuff', methods=['POST'])
def add_stuff():
    stuff_id = request.json['id']
    price = request.json['price']
    amount = request.json['amount']
    name = request.json['name']

    new_stuff = Stuff()
    new_stuff.id = stuff_id
    new_stuff.price = price
    new_stuff.amount = amount
    new_stuff.name = name

    db.session.add(new_stuff)
    db.session.commit()

    return str(new_stuff.__str__())


@app.route('/stuff/<id>', methods=['PUT'])
def stuff_update(id):
    price = request.json['price']
    amount = request.json['amount']
    name = request.json['name']

    new_stuff = Stuff.query.get(id)
    new_stuff.stuff_id = id
    new_stuff.price = price
    new_stuff.amount = amount
    new_stuff.name = name

    db.session.commit()

    return new_stuff.__str__()


@app.route('/stuff/<id>', methods=['DELETE'])
def stuff_delete(id):
    stuff = Stuff.query.get(id)
    db.session.delete(stuff)
    db.session.commit()

    return str("Deleting successful")
