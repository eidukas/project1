from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, HiddenField, BooleanField
from wtforms.widgets import Input
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class CheckboxInput(Input):
    input_type = 'checkbox'

    def __call__(self, field, **kwargs):
        if getattr(field, 'object_data', False):
            kwargs['checked'] = True
        return super(CheckboxInput, self).__call__(field, **kwargs)


class BooleanSubField(BooleanField):
    widget = CheckboxInput()


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
    quarterly_report = BooleanSubField('Quarterly report')
    submit = SubmitField('Create/Update')


class DeleteForm(FlaskForm):
    submit = SubmitField('Delete')
