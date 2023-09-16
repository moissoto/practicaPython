from flask import Flask, render_template, request, redirect
from vsearch import search4letters

app = Flask('Hola mundo')

@app.route('/')
def hello() ->'302':
    return redirect ('/entry')

@app.route('/search4',methods =['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form ['letters']
    title  = 'here are you results'
    results = str(search4letters(phrase,letters))
    return render_template('results.html', the_phrase= phrase, the_letters = letters,
                           the_title = title, the_results = results)
    "return str(search4letters('life, the universe, and everything','eiru'))"

@app.route('/entry')
def entry_page()->'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

app.run(debug = True)