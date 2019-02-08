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
    entry = CalendarEntry()
    print(form.id.data)
    if form.id.data is not '':
        entry.id = int(form.id.data)
    entry.Industry = form.industry.data
    entry.Date = form.date.data.isoformat(),
    entry.Event = form.event.data,
    entry.Ticker = form.ticker.data,
    print('entry', entry)
    # if new:
    #     print('new')
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
        album = CalendarEntry()
        save_changes(album, form, new=True)
        flash('Entry created successfully!')
        return redirect(url_for('calendar.index'))
    return render_template('calendar/create.html', form=form)

    # form = CreateUpdateEntryForm()
    # print('form', form)
    # if form.validate_on_submit():
    #     print('if')
    #     entry = CalendarEntry(Date=form.date.data,
    #                 Event=form.event.data,
    #                 Ticker=form.ticker.data,
    #                 Industry=form.industry.data)
    #     print('entry', entry)
    #     db.session.add(entry)
    #     db.session.commit()
    #     flash('Calendar entry was added')
    #     return redirect(url_for('calendar.index'))
    # print('else')
    # return render_template('calendar/create.html', form=form)


@calendar.route('/<id>/update', methods=['get', 'post'])
@login_required
def update(id):
    # @app.route('/item/<int:id>', methods=['GET', 'POST'])
    # def edit(id):
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
            # save edits
            save_changes(instance, form)
            flash('Calendar entry was updated')
            return redirect(url_for('calendar.index'))
        return render_template('calendar/update.html', form=form, entry_id=instance.id)
    else:
        return 'Error loading #{id}'.format(id=id)
    # instance = CalendarEntry.query.filter_by(id=id).first()
    # form = CreateUpdateEntryForm(instance)
    # if form.validate_on_submit():
    #     entry = CalendarEntry(Date=form.date.data,
    #                           Event=form.event.data,
    #                           Ticket=form.ticket.data,
    #                           Industry=form.industry.data)
    #     db.session.add(entry)
    #     db.session.commit()
    #     flash('Calendar entry was updated')
    #     return redirect(url_for('calendar.index'))
    # return render_template('calendar/update.html', form=form)


@calendar.route('/<int:id>/delete', methods=['post'])
@login_required
def delete(id):
    instance = CalendarEntry.query.filter_by(id=id).first()
    db.session.delete(instance)
    db.session.commit()
    flash('Calendar entry was deleted')
    return redirect(url_for('calendar.index'))


@calendar.route('/search', methods=['get'])
@login_required
def search():
    entries = CalendarEntry.query.all()

    return render_template('calendar/search.html', entries=entries)
