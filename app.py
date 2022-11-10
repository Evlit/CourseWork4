# Курсовая 4
# функция создания основного объекта app
from flask import Flask, render_template
from flask_restx import Api
#from flask_cors import CORS
from config import Config
from setup_db import db
from views.auth import auth_ns
from views.directors import director_ns
from views.genres import genres_ns
# from views.genre import genre_ns
from views.movies import movie_ns
from views.users import user_ns


def create_app(config_object):
    app = Flask(__name__)
#    CORS(app)
    app.config.from_object(config_object)

    @app.route('/')
    def index():
        return render_template('index.html')

    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genres_ns)
#    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
