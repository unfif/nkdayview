from flask import Flask, render_template, redirect, request
from model import Nkdayraces, init_db
import argparse as argp
import uvicorn

parser = argp.ArgumentParser()
parser.add_argument('-n', '--host', type=str, default='0.0.0.0')
parser.add_argument('-p', '--port', type=int, default=5000)
parser.add_argument('-l', '--log-level', type=str, default='info')
args = parser.parse_args()

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
db = init_db(app)

@app.route("/")
def getraces():
    data = Nkdayraces.getRaces()
    return render_template("index.html", **data)

if __name__ == '__main__':
    uvicorn.run(app, host=args.host, port=args.port, log_level=args.log_level, interface='wsgi', lifespan='off')
