import os
from flask_migrate import Migrate
from app import create_app, db
from app.models import User, Role, Book

app = create_app(os.getenv("FLASK_CONFIG") or 'default')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Book=Book)


# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

