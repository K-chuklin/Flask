from utils import load_candidates_from_json, get_candidates_by_name, get_candidates_by_skill
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    data = load_candidates_from_json()
    page = render_template("list.html")
    for candidate in data:
        number = candidate['id']
        page += f'<p><a href="/candidate/{number - 1}">' + candidate['name'] + '</p>'
    return page


@app.route('/candidate/<int:x>')
def candidate(x):
    data = load_candidates_from_json()
    page = render_template("card.html")
    url = data[x]['picture']
    page += '<h1>' + data[x]['name'] + '</h1>'\
            + '<p>' + data[x]['position'] + '</p>'\
            + f'<img src="{url}" width=200/>'\
            + '<p>' + data[x]['skills'] + '</p>'
    return page


@app.route('/search/<name>')
def search_by_name(name):
    data = get_candidates_by_name(name)
    page = render_template("search.html", candidates_counter=len(data))
    for candidate in data:
        number = candidate['id']
        page += '<p>' + f'<a href="/candidate/{number - 1}">' + f'{candidate["name"]}' + '<p>'
    return page


@app.route('/skill/<skill>')
def search_by_skill(skill):
    data = get_candidates_by_skill(skill)
    page = render_template("skill.html", candidates_counter=len(data))
    for candidate in data:
        number = candidate['id']
        page += '<p>' + f'<a href="/candidate/{number - 1}">' + f'{candidate["name"]}' + '<p>'
    return page


app.run()
