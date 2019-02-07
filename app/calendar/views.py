from flask import render_template, g

from flask_login import login_required, current_user


from .forms import SearchForm
from . import calendar

from ..models import CalendarEntry


@calendar.route('/', methods=['get'])
@login_required
def index():
    entries = CalendarEntry.query.all()

    return render_template('calendar/index.html', entries=entries)


@calendar.route('/search', methods=['get'])
@login_required
def search():
    entries = CalendarEntry.query.all()

    return render_template('calendar/search.html', entries=entries)
