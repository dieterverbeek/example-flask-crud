import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'do-or-do-not-there-is-no-try')  # Gebruik een omgevingsvariabele voor de SECRET_KEY

    # Zorg ervoor dat je de juiste database-parameters hier invult.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
