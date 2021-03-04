from app import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(30), nullable=True)
    home = db.relationship('House', backref='person')
    owner = db.relationship('ownership', backref='person')

class House(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(25), nullable=False)
    street = db.Column(db.String(15), nullable=False)
    market_price = db.Column(db.Float, nullable=True)
    owner_id= db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    owner = db.relationship('ownership', backref='house')

class ownership(db.Model):
    landlord_register = db.Column(db.Integer, primary_key=True)
    owner = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    propperty = db.Column(db.Integer, db.ForeignKey('house.id'), nullable=False)
    price = db.Column(db.Integer, nullable=False)





# DataIn = Person(name='Daniel', surname='Diaz Souto')
# MoreData = Person(name='Nadia', surname='Peruffo')
# ExtraData = Person(name='Diego', surname='Diaz Peruffo')

#db.session.add(ExtraData)
#db.session.commit()