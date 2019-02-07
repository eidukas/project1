from flask import render_template, g

from flask_login import login_required, current_user


from .forms import SearchForm
from . import calendar

# from ..models import CalendarEntry


# @calendar.route('/')
# @login_required
# def index():
#     return render_template('calendar/index.html')


@calendar.route('/search')
@login_required
def index():
    return render_template('calendar/search.html')
