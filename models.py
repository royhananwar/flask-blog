from setup import *
import datetime


class Post(db.Model):
    __tablename__ = 'post'

    id_post = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    text = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return 'Title : %r ' % (self.title,)


db.create_all()