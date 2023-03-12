from flask import Flask
from utils import load_candidates, get_all, get_by_skill

app = Flask(__name__)


@app.route('/')
def index():
    info = load_candidates()
    result = ''
    for data in info:
        result += '<pre>' + data['name'] + '</pre>'
        result += '<pre>' + data['position'] + '</pre>'
        result += '<pre>' + data['skills'] + '</pre>' + '<br>'
    return result


@app.route('/candidate/<int:x>')
def candidate(x):
    data = get_all()
    result = ''
    url = data[x]['picture']
    result += '<pre>' + data[x]['name'] + '</pre>' \
              + '<pre>' + data[x]['position'] + '</pre>' \
              + '<pre>' + data[x]['skills'] + '</pre>'
    return f'<img src="{url}"> {result}'


@app.route('/skills/<x>')
def skills(x):
    data = get_by_skill(x)
    result = ''
    i = 0
    while i <= len(data)-1:
        result += '<pre>' + data[i]['name'] + '</pre>' \
                + '<pre>' + data[i]['position'] + '</pre>' \
                + '<pre>' + data[i]['skills'] + '</pre>' + '<br>'
        i += 1
    return result


app.run()
