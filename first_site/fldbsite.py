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
    return render_template('index.html', menu=dbase.get_menu(),
                           posts=dbase.get_post_annonce())


@app.route('/about')
def about():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('about.html', menu=dbase.get_menu(),
                           posts=dbase.get_post_annonce(), title='О нас')


@app.route("/posts/<int:id_post>")
def posts(id_post):
    db = get_db()
    dbase = FDataBase(db)

    post = dbase.get_post(id_post)
    if not post:
        return "Пост не найден", 404

    name, price, data_limit, call_minutes, validity_period = post
    return render_template("posts.html", title=name, menu=dbase.get_menu(),
                           post={
                               'name': name,
                               'price': f"{price} руб",
                               'data_limit': f"{data_limit} ГБ",
                               'call_minutes': f"{call_minutes} мин.",
                               'validity_period':  f"{validity_period} дней"
                           })


@app.route('/add_post', methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == "POST":
        name = request.form['name']
        price = float(request.form['price'])
        data_limit = int(request.form['data_limit'])
        call_minutes = int(request.form['call_minutes'])
        validity_period = int(request.form['validity_period'])

        if len(name) < 2:
            flash('Пожалуйста, укажите название тарифа более 1 символа.', 'error')
            return redirect(url_for('add_post'))
        if price < 1:
            flash('Пожалуйста, введите корректную цену.', 'error')
            return redirect(url_for('add_post'))
        if data_limit < 1:
            flash('Пожалуйста, введите корректный лимит данных.', 'error')
            return redirect(url_for('add_post'))
        if call_minutes < 1:
            flash('Пожалуйста, введите корректное количество минут.', 'error')
            return redirect(url_for('add_post'))
        if validity_period < 1:
            flash('Пожалуйста, введите корректный срок действия.', 'error')
            return redirect(url_for('add_post'))

        res = dbase.add_post(name, price, data_limit, call_minutes, validity_period)
        if not res:
            flash('Ошибка добавления данных')
        else:
            flash('Тариф успешно добавлен.', 'success')
            # return redirect(url_for('index'))

    return render_template('add_post.html', title='Добавить тариф', menu=dbase.get_menu())


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
