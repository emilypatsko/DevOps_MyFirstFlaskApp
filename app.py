from re import L
from flask import Flask, render_template, request

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