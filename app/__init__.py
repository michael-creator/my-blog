from flask import Flask
from flask_bootstrap import Bootstrap

def create_app(config_name):
    app = Flask(__name__)

app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")


bootstrap = Bootstrap(app)
...