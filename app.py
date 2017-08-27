from flask import Flask
from flask import render_template
from flask import request
from model import MovieWebDAO
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

@app.route('/search/<keyword>')
def search(keyword=None):
    return render_template('list.html', functionPath="search", keyword=keyword)

@app.route('/favor/')
def favor():
    return render_template('list.html', functionPath="favor")

@app.route('/api/recently/')
def getRecentlyMovies():
    start = request.args.get("start", type=int, default=0)
    limit = request.args.get("limit", type=int, default=10)

    #print(str(start) + ", " + str(limit))

    movies = MovieWebDAO.getRecentlyMovies(start, limit)
    total = MovieWebDAO.countRecentlyMovies()
    return json.dumps({"movies": movies, "total": total}, ensure_ascii=False)

@app.route('/api/recommander/')
def getRecommanderMovies():
    start = request.args.get("start", type=int, default=0)
    limit = request.args.get("limit", type=int, default=10)

    movies = Forcast.forcastMovies(start, limit)
    total = Forcast.countForcastMovies()
    return json.dumps({"movies": movies, "total": total}, ensure_ascii=False)

@app.route('/api/download/')
def getDownloadMovies():
    start = request.args.get("start", type=int, default=0)
    limit = request.args.get("limit", type=int, default=10)

    movies = MovieWebDAO.getDownloadMovies(start, limit)
    total = MovieWebDAO.countDownloadMovies();

    return json.dumps({"movies": movies, "total": total}, ensure_ascii=False)


@app.route('/api/search/<keyword>')
def getSearchMovies(keyword=None):
    start = request.args.get("start", type=int, default=0)
    limit = request.args.get("limit", type=int, default=10)

    movies = MovieWebDAO.getSearchMovies(start, limit, keyword)
    total = MovieWebDAO.countSearchMovies(keyword)
    return json.dumps({"movies": movies, "total": total}, ensure_ascii=False)

@app.route('/api/favor/')
def getFavorMovies():
    start = request.args.get("start", type=int, default=0)
    limit = request.args.get("limit", type=int, default=10)

    movies = MovieWebDAO.getFavorMovies(start, limit)
    total = MovieWebDAO.countFavorMovies();

    return json.dumps({"movies": movies, "total": total}, ensure_ascii=False)

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
    app.run(host='0.0.0.0', debug=True, port=15001)