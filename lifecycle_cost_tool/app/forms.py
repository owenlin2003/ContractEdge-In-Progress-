from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField, FloatField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed, FileRequired

class ContractForm(FlaskForm):
    year = StringField('Year', validators=[DataRequired()])
    obligation_amount = FloatField('Obligation Amount', validators=[DataRequired()])
    description = StringField('Description')
    submit = SubmitField('Add Contract')

class UploadForm(FlaskForm):
    file = FileField('Upload CSV', validators=[
        FileRequired(),
        FileAllowed(['csv'], 'CSV files only!')
    ])
    submit = SubmitField('Upload')

