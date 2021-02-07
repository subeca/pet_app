#!/usr/bin/python3

import unittest
from flask import url_for
from flask_testing import TestCase
from app import app
from application import app, db
from application.models import Person, Pet

class TestBase(TestCase):
    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                DEBUG=True,
                WTF_CSRF_ENABLED = False
                )
        return app

    def setUp(self):
        db.create_all()
        exampleperson = Person(name = "Harry")
        examplepet = Pet(name = "Luna", person = exampleperson)

        db.session.add(exampleperson)
        db.session.add(examplepet)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_home_get(self):
        response = self.client.get(url_for('home'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_review_get(self):
        response = self.client.get(url_for('review'))
        self.assertEqual(response.status_code, 200)

    def test_add_get(self):
        response = self.client.get(url_for('add'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
                
class TestAdd(TestBase):

    def test_add_post(self):
        self.client.post(url_for('add'), data=dict(name = "James", person = "person"), follow_redirects=True)
        response = self.client.get(url_for('review'))
        self.assertIn(b'James', response.data)

class TestUpdate(TestBase):
    def test_update_post(self):
        self.client.post(url_for('update'), data=dict(oldname="Puppy", newname="Kitten"), follow_redirects=True)
        self.assertIn(b'Kitten', response.data)

class TestDelete(TestBase):
    def test_delete_post(self):
        self.client.post(url_for('delete'), data=dict(petname="Puppy", person = "Harry"), follow_redirects=True)
        response = self.client.get(url_for('review'))
        self.assertEqual(response.status_code, 200)