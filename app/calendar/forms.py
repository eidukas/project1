from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectMultipleField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])


class FilterForm(FlaskForm):
    date_from = DateField('From', default=datetime.today(), validators=[DataRequired()])
    date_to = DateField('To', validators=[DataRequired()])
    industries = SelectMultipleField('Industries', default='__all__', validators=[DataRequired()])


