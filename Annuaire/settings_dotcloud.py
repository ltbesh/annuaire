import json
 
with open('/home/dotcloud/environment.json') as f:
    env = json.load(f)
 
from .settings import *
 
with open('/home/dotcloud/environment.json') as f:
  env = json.load(f)

DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'annuaire',
    'USER': env['DOTCLOUD_DB_SQL_LOGIN'],
    'PASSWORD': env['DOTCLOUD_DB_SQL_PASSWORD'],
    'HOST': env['DOTCLOUD_DB_SQL_HOST'],
    'PORT': int(env['DOTCLOUD_DB_SQL_PORT']),
}
}
