#!/usr/bin/python3

#!/usr/bin/python3

from flask_wtf import FlaskForm
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from application.models import Pet

class Add(FlaskForm):
    personname = StringField('Person Name', validators=[DataRequired()])
    petname = StringField('Pet Name', validators=[DataRequired()])
    submit = SubmitField('Add Pet')

def selectlist():
    return Pet.query

class Update(FlaskForm):
    petname = QuerySelectField('Select Pet to Delete', query_factory=selectlist, allow_blank=True, get_label='name')
    newname = StringField('New Pet Name', validators=[DataRequired()])
    submit = SubmitField("Update Pet")

class Delete(FlaskForm):
    petname = QuerySelectField('Select Pet to Delete', query_factory=selectlist, allow_blank=True, get_label='name')
    submit = SubmitField("Delete Pet")


