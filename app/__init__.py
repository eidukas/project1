from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
#    engine = create_engine(os.getenv("DATABASE_URL"))
#    db = scoped_session(sessionmaker(bind=engine))



    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .books import books as books_blueprint
    app.register_blueprint(books_blueprint, url_prefix='/books')

    from .calendar import calendar as calendar_blueprint
    app.register_blueprint(calendar_blueprint, url_prefix='/calendar')

    return app






