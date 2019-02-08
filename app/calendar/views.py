from flask import render_template, g, flash, redirect, url_for, request

from flask_login import login_required, current_user


from .forms import SearchForm, CreateUpdateEntryForm
from . import calendar
from .. import db

from ..models import CalendarEntry


@calendar.route('/', methods=['get'])
@login_required
def index():
    entries = CalendarEntry.query.all()

    return render_template('calendar/index.html', entries=entries)


def save_changes(entry, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    entry.Industry = form.industry.data
    entry.Event = form.event.data
    entry.Date = form.date.data
    entry.Ticker = form.ticker.data
    print('entry', entry)
    if form.id.data is not '':
        entry.id = int(form.id.data)
    else:
        # Add the new album to the database
        db.session.add(entry)

    # commit the data to the database
    db.session.commit()


@calendar.route('/add', methods=['GET', 'POST'] )
@login_required
def create():
    print('create entry')
    form = CreateUpdateEntryForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the entry
        entry = CalendarEntry()
        save_changes(entry, form)
        flash('Entry created successfully!')
        return redirect(url_for('calendar.close'))
    return render_template('calendar/create.html', form=form)


@calendar.route('/<id>/update', methods=['get', 'post'])
@login_required
def update(id):
    instance = CalendarEntry.query.filter_by(id=id).first()

    if instance:
        form = CreateUpdateEntryForm(data={'id': str(instance.id),
                                           'event': instance.Event,
                                           'industry': instance.Industry,
                                           'date': instance.Date,
                                           'ticker': instance.Ticker,},
                                     obj=instance,
                                     formdata=request.form)
        print('form', form.ticker, form.industry)
        if request.method == 'POST' and form.validate():
            form.populate_obj(instance)
            save_changes(instance, form)
            flash('Calendar entry was updated')
            return redirect(url_for('calendar.close'))
        return render_template('calendar/update.html', form=form, entry_id=instance.id)
    else:
        return 'Error loading #{id}'.format(id=id)


@calendar.route('/<int:id>/delete', methods=['post'])
@login_required
def delete(id):
    instance = CalendarEntry.query.filter_by(id=id).first()
    db.session.delete(instance)
    db.session.commit()
    flash('Calendar entry was deleted')
    return redirect(url_for('calendar.index'))



@calendar.route('/done', methods=['get'])
@login_required
def close():
    return render_template('calendar/empty.html')

def filterdate(r):
    return r.strftime('%Y-%m-%d')


@calendar.route('/search', methods=['get'])
@login_required
def search():
    entries = CalendarEntry.query.all()

    return render_template('calendar/search.html', entries=entries, filterdate=filterdate)
