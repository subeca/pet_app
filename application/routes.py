#!/usr/bin/python3

from application import app, db
from application.models import Person, Pet 
from flask import Flask, render_template, request, url_for, redirect
from application.forms import Add, Delete, Update

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/review', methods=['GET'])
def review():
    petlist = Pet.query.with_entities(Pet.name)
    return render_template('review.html', petlist = petlist) 

@app.route('/add', methods=['GET', 'POST'])
def add():
    error = ""
    form = Add()

    if request.method == 'POST':
        personname = form.personname.data
        petname = form.petname.data

        person = Person(name = personname)
        db.session.add(person)
        db.session.commit()
        pet = Pet(name = petname, person = Person.query.filter_by(name=personname).first())
        db.session.add(pet)
        db.session.commit()

        if len(personname) == 0 or len(petname) == 0:
            error = "Please enter your name and the pet's name"
        else:
            return redirect(url_for('home'))

    return render_template('add.html', form=form, message=error)


@app.route('/update', methods=['GET', 'POST'])
def update():
    error = ""
    form = Update()

    if request.method == 'POST':
        petname = form.petname.data
        newname = form.newname.data
        petname.name = newname
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('update.html', form=form, message=error)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    error = ""
    form = Delete()

    if request.method == 'POST':
        petname = form.petname.data
        db.session.delete(petname)
        db.session.commit()
        return "Pet name has been successfully deleted"
    
    return render_template('delete.html', form=form, message=error)
