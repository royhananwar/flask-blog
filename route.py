from flask import render_template, redirect, url_for, request
from models import *


@app.route('/secret')
def view_portofolio():
    return render_template('secret/index.html')


@app.route('/')
def homepage():
    posts = Post.query.order_by(Post.date.desc()).all()
    return render_template('blog/homepage.html', posts=posts)


@app.route('/new_post/')
def sample_post():
    return render_template('blog/new_post.html')


@app.route('/post/<id_post>')
def show_post(id_post):
    post = Post.query.filter(Post.id_post == id_post).first()
    return render_template('blog/show_post.html', post=post)


@app.route('/add_post/', methods=['post'])
def add_post():
    post = Post(title=request.form['title'], text=request.form['text'])
    db.session.add(post)
    db.session.commit()

    return redirect(url_for('homepage'))


