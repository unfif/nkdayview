from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
# from flask_sqlalchemy_session import flask_scoped_session
from models import Nkdayraces#, Session
from settings import env

import argparse as argp
import uvicorn

parser = argp.ArgumentParser()
parser.add_argument('-n', '--host', type=str, default='0.0.0.0')
parser.add_argument('-p', '--port', type=int, default=5000)
parser.add_argument('-l', '--log-level', type=str, default='info')
args = parser.parse_args()

DATABASE_URL = env.get('DATABASE_URL')
# SQLITE_URL = env.get('SQLITE_URL')
# MONGO_URL = env.get('MONGO_URL')

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
# session = flask_scoped_session(Session, app)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
data = Nkdayraces.getRaces()

@app.route('/')
def getraces():
    # print(session.query(Nkdayraces))
    return render_template('index.html', **data)

if __name__ == '__main__':
    uvicorn.run(app, host=args.host, port=args.port, log_level=args.log_level, interface='wsgi', lifespan='off')
