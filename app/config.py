import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'do-or-do-not-there-is-no-try'
#    SECRET_KEY = os.environ.get('SECRET_KEY') or 'do-or-do-not-there-is-no-try'
    SQLALCHEMY_DATABASE_URI = os.environ.get('database-1.cb2sm4wk4177.us-east-1.rds.amazonaws.com') or 'mysql://admin:<adminproject>@database-1.cb2sm4wk4177.us-east-1.rds.amazonaws.com/<project>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
