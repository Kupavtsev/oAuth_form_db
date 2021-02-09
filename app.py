try:
    from flask import Flask, render_template, url_for, request, redirect, make_response
    import json
    from time import time
    from flask import Flask, render_template, make_response
    from flask_dance.contrib.github import make_github_blueprint, github
    import logging
    import psycopg2

    import config
    from models import Storage, BlogPostModel
    from forms import BlogPostForm, DB_Form

except Exception as e:
    print("Some Modules are Missings {}".format(e))

logger = logging.getLogger(__name__)


# Connect to DataBase

try:
    conn = psycopg2.connect(
        user='postgres',
        password='123456',
        database='emphabd',
        host='localhost',
        port=5432,
    )
except Exception as ex:
    print('-----I am unable to connect to the database-----', ex)
    raise ex

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)


# oAuth2.0 GitHub connection

github_blueprint = make_github_blueprint(client_id='a12c5ae7e06321b15813',
                                         client_secret='example')

app.register_blueprint(github_blueprint, url_prefix='/github_login')


# Routes
# If you authorized, you'll get on registration form page
@app.route('/')
def github_login():

    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        return home()

    return '<h1>Request failed!</h1>'


# Main registration form
@app.route('/form/', methods=['GET', 'POST'])
def home():
    cur = conn.cursor()

    storage = Storage()
    all_items = storage.items

    if request.method == 'POST':
        # Show data on a the page, lower than form
        form = BlogPostForm(request.form)
        if form.validate():
            model = BlogPostModel(form.data)
            all_items.append(model)
            print('valid', 200)
        else:
            logger.error('Wrong form!')
            print('invalid', 400)
    
        # Saving data to DB
        db_form = DB_Form(request.form)
        if db_form.validate():
            username = db_form.username.data
            text = db_form.text.data
            cur.execute(
                """INSERT INTO public.users(
                username, text) VALUES (
                %(username)s, %(text)s)""",
                {'username': username, 'text': text}
            )
            conn.commit()
    else:
        form = BlogPostForm()

    return render_template(
        'home.html',
        form=form,
        items=all_items,
    )

# List of all registred users
# get this data from DB
@app.route('/list', methods=['GET'])
def users_list():
    cur = conn.cursor()
    cur.execute(
            """SELECT * from public.users;"""
        )
    data = cur.fetchall()
    response = make_response(json.dumps(data))
    return response

if __name__ == "__main__":
    app.run()
