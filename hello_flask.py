from flask import Flask
from vsearch import search4letters

app = Flask('Hola mundo')

@app.route('/')
def hello() ->str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything','eiru'))

app.run()