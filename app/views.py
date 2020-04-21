from flask import render_template,redirect, url_for, request
from app import app
from .request import getMovies, search_movie
from .models import review
from .forms import ReviewForm
Review = review.Review

@app.route('/')
def index():
    title ="Welcome to thr number one  movie shop"
    popular_movies = getMovies('popular')
    upcoming_movie = getMovies('upcoming')
    now_showing_movie = getMovies('now_playing')
    search_movie = request.args.get('movie_query')
    if search_movie:
        return redirect(url_for('search', movie_name = search_movie))
    else:
        return render_template('index.html', title = title, popular= popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)

@app.route('/search/<movie_name>')
def search(movie_name):
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movie = search_movie(movie_name_format)
    title = {movie_name}
    return render_template('search.html', movies= searched_movie)

@app.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    movie = get_movie(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(movie.id,title,movie.poster,review)
        new_review.save_review()
        return redirect(url_for('movie',id = movie.id ))

    title = {movie.title} 
    return render_template('new_review.html',title = title, review_form=form, movie=movie)

@app.route('/movie/<int:id>')
def movie(id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = {movie.title}
    reviews = Review.get_reviews(movie.id)

    return render_template('movie.html',title = title,movie = movie,reviews = reviews)

