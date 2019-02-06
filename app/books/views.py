from flask import render_template

from flask_login import login_required

from . import books

from ..models import Book


@books.route('/')
@login_required
def index():
    books = Book.query.all()

    # db = get_db()
    # books = db.execute(
    #     'SELECT id, isbn, title, author, year'
    #     ' FROM books '
    # ).fetchall()
    return render_template('books/index.html', books=books)

