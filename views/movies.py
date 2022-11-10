# Представление для фильмов
from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    """
    Класс фильмов
    """
#    @auth_required
    def get(self):
        """
        Вывод всех фильмов или по условию
        """
        status = request.args.get("status")
        page = int(request.args.get("page", 0))
        filters = {
            "status": status,
            "page": page,
        }
        all_movies = movie_service.get_all(filters)
        res = MovieSchema(many=True).dump(all_movies)
        return res, 200


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    """
    Класс фильм
    """
#    @auth_required
    def get(self, mid):
        """
        Вывод фильма по id
        """
        one_movie = movie_service.get_one(mid)
        res = MovieSchema().dump(one_movie)
        return res, 200
