DEBUG = True
SECRET_KEY = 'SecretKey'
WTF_CSRF_ENABLED = False

try:
    from config_local import *
except ImportError:
    pass
