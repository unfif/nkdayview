#Usage

```python app.py --host=0.0.0.0 -p 5000```
web python app.py --host=0.0.0.0 -p $PORT

```flask run --debugger --reload```
web flask run --host=0.0.0.0 --port=$PORT

$env:PYTHONPATH = "."

```twistd web --wsgi app.app --listen=tcp:5000```
web twistd web --wsgi app.app --listen=tcp:$PORT
