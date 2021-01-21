from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

class BlogPostForm(FlaskForm):
    title = StringField(label='Title', validators=[
        validators.Length(min=4, max=140)
    ])
    text = StringField(label='Article Text', validators=[
        validators.Length(min=10, max=3500)
    ])
    author = StringField(label='Author', validators=[
        validators.Length(min=4, max=140)
    ])