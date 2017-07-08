from flask import Flask
from flask import render_template
from web.model import MovieWebDAO
import json
from ml import Forcast

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/recently/')
def recently():
    return render_template('list.html', functionPath="recently")

@app.route('/download/')
def download():
    return render_template('list.html', functionPath="download")

@app.route('/recommander/')
def recommander():
    return render_template('list.html', functionPath="recommander")

@app.route('/api/recently/')
def getRecentlyMovies():
    movies = MovieWebDAO.getRecentlyMovies(0, 200)
    return json.dumps(movies, ensure_ascii=False)

@app.route('/api/recommander/')
def getRecommanderMovies():
    movies = Forcast.forcastMovies()
    return json.dumps(movies, ensure_ascii=False)

@app.route('/api/download/')
def getDownloadMovies():
    movies = MovieWebDAO.getDownloadMovies(0, 200)
    return json.dumps(movies, ensure_ascii=False)

@app.route('/api/pick/<actor>/<avNumber>')
def pick(actor=None, avNumber=None):
    if not actor or not avNumber:
        return "must be <actor>/<avNumber>"

    MovieWebDAO.downloadMovie(avNumber)
    #DiskIndex.copyOneImageToTemp(actor, avNumber)
    return "OK"

@app.route('/api/skip/<avNumber>')
def skip(avNumber=None):
    MovieWebDAO.skipMovie(avNumber)
    return "OK"


if __name__ == '__main__':
    app.run()