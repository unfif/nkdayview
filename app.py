from flask import Flask, render_template, redirect, request
from model import Nkdayraces, init_db#, ToDoList
import argparse as argp
import uvicorn

parser = argp.ArgumentParser()
parser.add_argument('-n', '--host', type=str, default='127.0.0.1')
parser.add_argument('-p', '--port', type=int, default=5000)
parser.add_argument('-l', '--log-level', type=str, default='info')
args = parser.parse_args()

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
db = init_db(app)
# todolist = ToDoList()

@app.route("/")
def getraces():
    data = Nkdayraces.getRaces()
    return render_template("index.html", **data)

# @app.route("/todo")
# def show_todolist():
#     return render_template("index.html", todolist=todolist.get_all())
#
# @app.route("/additem", methods=["POST"])
# def add_item():
#     title = request.form["title"]
#     if not title:
#         return redirect("/")
#
#     todolist.add(title)
#     return redirect("/")
#
# @app.route("/deleteitem/<int:item_id>")
# def delete_todoitem(item_id):
#     todolist.delete(item_id)
#     return redirect("/")
#
# @app.route("/deletealldoneitems")
# def delete_alldoneitems():
#     todolist.delete_doneitem()
#     return redirect("/")
#
# @app.route("/updatedone", methods=["POST"])
# def update_done():
#     keys = request.form.keys()
#     items = [int(x) for x in keys]
#     todolist.update_done(items)
#     return redirect("/")
#
# @app.route("/favicon.ico")
# def favicon():
#     return app.send_static_file("favicon.ico")

# if __name__ == '__main__':
#     app.run(debug=False, host='0.0.0.0')

if __name__ == '__main__':
    uvicorn.run(app, host=args.host, port=args.port, log_level=args.log_level, interface='wsgi')
