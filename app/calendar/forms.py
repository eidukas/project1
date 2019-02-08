from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, HiddenField
from wtforms.fields.html5 import DateField, DateTimeField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])


class FilterForm(FlaskForm):
    date_from = DateField('From', default=datetime.today(), )
    date_to = DateField('To', )
    industries = SelectMultipleField('Industries', default='__all__', )


class CreateUpdateEntryForm(FlaskForm):
    id = HiddenField('id')
    date = DateField('Date', validators=[DataRequired()])
    event = StringField('Event', validators=[DataRequired()])
    industry = StringField('Industry', validators=[DataRequired()])
    ticker = StringField('Ticker', validators=[DataRequired()])
    submit = SubmitField('Create/Update')


class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')
