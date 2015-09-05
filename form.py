from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class IssuesForm(Form):
    environment = BooleanField('environment', default=True)
    lgbtq = BooleanField('lgbtq', default=False)
    poverty = BooleanField('poverty', default=False)
    immigration = BooleanField('immigration', default=False)


class UserDataForm(Form):
    name = StringField('name', validators=[DataRequired()])
    whyvisiting = StringField('whyvisiting', validators=[DataRequired()])
    #add other fields later (e.g. Gender, Hometown, Occupation, Age)
