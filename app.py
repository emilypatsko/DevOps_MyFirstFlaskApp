from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/films/list')
def get_films_list():
    return render_template('films_list.html')

@app.route('/films/table')
def get_films_table():
    with open('films.csv', 'r') as f:
        lines = f.read().splitlines()
        lines = [line.split(',') for line in lines]
        films = [{'title': line[0], 'rating': line[1]} for line in lines]
    stars = request.values.get("stars", "")
    if stars != "":
        films = [film for film in films if film['rating'] == stars]
    return render_template('films_table.html', films=films)

@app.route('/films/submit')
def get_rating_form():
    return render_template('rating_form.html')

@app.route('/films/submit', methods=['POST'])
def add_rating():
    filmname = request.form['filmname']
    stars = request.form['stars']
    with open('films.csv', 'a') as f:
        f.write(f"{filmname},{stars}\n")
    return redirect('/films/submit')