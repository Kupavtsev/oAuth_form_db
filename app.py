try:
    from flask import Flask, render_template, url_for, request, redirect, make_response
    import random
    import json
    from time import time
    from random import random
    from flask import Flask, render_template, make_response
    from flask_dance.contrib.github import make_github_blueprint, github
    import logging

    import config
    from models import Storage, BlogPostModel
    from forms import BlogPostForm
except Exception as e:
    print("Some Modules are Missings {}".format(e))

logger = logging.getLogger(__name__)

app = Flask(__name__, template_folder='templates')
app.config.from_object(config)
# app.config["SECRET_KEY"]="SECRET KEY  "

github_blueprint = make_github_blueprint(client_id='a12c5ae7e06321b15813',
                                         client_secret='186c69aa548fbcdd8d9ec1780df87e86ad729cc4')

app.register_blueprint(github_blueprint, url_prefix='/github_login')


@app.route('/')
def github_login():

    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        # account_info = github.get('/user')
        # if account_info.ok:
        #     account_info_json = account_info.json()
        #     return '<h1>Your Github name is {}'.format(account_info_json['login'])
        return home()

    return '<h1>Request failed!</h1>'


@app.route('/data', methods=["GET", "POST"])
def data():
    data = [time() * 1000, random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


@app.route('/form/', methods=['GET', 'POST'])
def home():

    storage = Storage()
    all_items = storage.items

    if request.method == 'POST':
        form = BlogPostForm(request.form)
        if form.validate():
            model = BlogPostModel(form.data)
            all_items.append(model)
            print('valid', 200)
        else:
            logger.error('Wrong form!')
            print('invalid', 400)
    # elif request.method == 'GET':
    #     return 'hello world!', 200
    else:
        form = BlogPostForm()

    return render_template(
        'home.html',
        form=form,
        items=all_items,
    )


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
