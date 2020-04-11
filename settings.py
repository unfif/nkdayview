import os
import pathlib as pl
from dotenv import load_dotenv

envpath = (pl.Path(__file__).with_name('.env')).resolve()
load_dotenv(envpath)
env = os.environ

DATABASE_URL = env.get('DATABASE_URL')
SQLITE_URL = env.get('SQLITE_URL')
# MONGO_URL = env.get('MONGO_URL')
if DATABASE_URL is None:
    if SQLITE_URL is None:
        env['DATABASE_URL'] = "sqlite:///nkdayraces.sqlite3"
    else:
        env['DATABASE_URL'] = SQLITE_URL
