from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class PetForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    age = IntegerField('Age', validators=[DataRequired()])
    type = SelectField('Type', choices=[
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    submit = SubmitField('Add Pet')
