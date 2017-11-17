import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#print(SQLALCHEMY_MIGRATE_REPO)

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [{'name': 'Yahoo', 'url': 'https://me.yahoo.com'}]

