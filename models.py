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
        