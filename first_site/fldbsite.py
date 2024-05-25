import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, g
from FDataBase import FDataBase

DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = '7b5bfa1c1d944d03fe1eb3fa7e74d9eb5f658839'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, 'flsk.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/')
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu())


@app.route('/all_posts')
def all_posts():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('all_posts.html', menu=dbase.get_menu(), title='Все статьи')


@app.route('/about')
def about():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('about.html', menu=dbase.get_menu(), title='О нас')


@app.route('/signup', methods=["POST", "GET"])
def signup():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('signup.html', menu=dbase.get_menu(), title='Регистрация')


@app.route('/login', methods=["POST", "GET"])
def login():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('login.html', menu=dbase.get_menu(), title='Вход')


@app.route('/profile')
def profile():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('profile.html', menu=dbase.get_menu(), title='Профиль')


@app.route('/add_post', methods=["POST", "GET"])
def add_post():
    if request.method == "POST":
        title = request.form['title']
        if len(title.strip()) > 1:
            flash('Статья успешно добавлена.', category='success')
        else:
            flash('Заголовок должен содержать как минимум 2 символа.', category='error')
            return redirect(url_for('add_post'))
    db = get_db()
    dbase = FDataBase(db)
    return render_template('add_post.html', title='Добавить статью', menu=dbase.get_menu())


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template("page404.html", title="Страница не найдена", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == "__main__":
    app.run(debug=True)
