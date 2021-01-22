from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Storage():
    items = None
    _obj = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls)
            cls.items = []
        return cls._obj

class BlogPostModel():
    def __init__(self, form_data):
        self.username = form_data['username']
        self.text = form_data['text']


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(40), unique=True)
#     text = db.Column(db.String(640), unique=False)

#     def get_user_id(self):
#         return self.id

#     def __str__(self):
#         return self.username

#     def __str__(self):
#         return self.text
        