from flask import render_template
from app import app
from .request import getMovies

@app.route('/')
def index():
    title ="Welcome to thr number one  movie shop"
    popular_movies = getMovies('popular')
    upcoming_movie = getMovies('upcoming')
    now_showing_movie = getMovies('now_playing')
    print(popular_movies)
    return render_template('index.html', title = title, popular= popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)
