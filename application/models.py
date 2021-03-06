#!/usr/bin/python3

from application import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pet = db.relationship('Pet', backref='person')

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)


    def __repr__(self, name):
        self.name = name
        return '[Pet {}]'.format(self.name) 
