# oAuth 2.0 Provider with Form and SQlite

```bash
$ pip install -r requirements.txt
```

Set Flask and Authlib environment variables:

```bash
# disable check https (DO NOT SET THIS IN PRODUCTION)
$ export OUTHLIB_INSECURE_TRANSPORT=1
```

Create Database and run the development server:

```bash
$ flask run
$ python app.py
```

Now, you can open your browser with `http://127.0.0.1:5000/`