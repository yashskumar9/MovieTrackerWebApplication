from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
movie_api = os.getenv('MOVIE_API')
movie_info_url = os.getenv('MOVIE_INFO_URL')
movie_image_url = os.getenv('MOVIE_IMAGE_URL')

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE
class Movies(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


class EditForm(FlaskForm):
    new_rating = StringField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired()])
    new_review = StringField('Your Review', validators=[DataRequired(), length(max=250)])
    submit = SubmitField('Done')


class AddMovieForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired(), length(max=250)])
    submit = SubmitField('Add Movie')


def check_title(movie_name):
    movie_list = db.session.execute(db.select(Movies)).scalars().all()
    for movie in movie_list:
        if movie.title.lower() == movie_name.lower():
            return False
    return True


@app.route("/")
def home():
    movie_list = db.session.execute(db.select(Movies).order_by(Movies.rating)).scalars().all()

    for i in range(len(movie_list)):
        movie_list[i].ranking = len(movie_list) - i
    db.session.commit()
    all_movie = db.session.execute(db.select(Movies).order_by(Movies.ranking)).scalars().all()

    return render_template("index.html", movies=all_movie)


@app.route('/edit/<int:edit_id>', methods=['POST', 'GET'])
def edit(edit_id):
    form = EditForm()
    edit_movie = db.get_or_404(Movies, edit_id)
    if form.validate_on_submit():
        edit_movie.rating = form.new_rating.data
        edit_movie.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', form=form, movie=edit_movie)


@app.route('/delete/<int:delete_id>')
def delete(delete_id):
    delete_movie = db.get_or_404(Movies, delete_id)
    db.session.delete(delete_movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/add_movie', methods=['POST', 'GET'])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_name = form.movie_title.data
        response = requests.get(movie_api, params={"query": movie_name, "api_key": api_key}).json()
        if response.get('results'):
            movie_names = response['results']
            return render_template('select.html', options=movie_names)
        else:
            flash("No movies found for your search. Please try again!", "danger")
            return redirect(url_for('add_movie'))
    return render_template('add.html', form=form)


@app.route('/find_movie')
def find_movie():
    movie_api_id = request.args.get('id')
    movie = request.args.get('movie')
    if check_title(movie):
        if movie_api_id:
            movie_api_url = f'{movie_info_url}/{movie_api_id}'
            response = requests.get(movie_api_url, params={'api_key': api_key, 'language': 'en-US'})
            data = response.json()
            new_movie = Movies(
                title=data['title'],
                year=data['release_date'].split('-')[0],
                description=data['overview'],
                img_url=f"{movie_image_url}{data['poster_path']}"
            )
            with app.app_context():
                db.session.add(new_movie)
                db.session.commit()
                new_movie_id = new_movie.id

            return redirect(url_for('edit', edit_id=new_movie_id))
    else:
        flash(f'"{movie}" already exist!', 'warning')
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
