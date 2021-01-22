from flask_wtf import FlaskForm
from wtforms import StringField, validators, ValidationError

class BlogPostForm(FlaskForm):
    username = StringField(label='Username', validators=[
        validators.Length(min=4, max=140)
    ])
    text = StringField(label='Text', validators=[
        validators.Length(min=10, max=3500)
    ])
    