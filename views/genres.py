from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    """
    Класс жанров
    """
    def get(self):
        """
        Вывод всех жанров
        """
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200


@genres_ns.route('/<int:gid>')
class GenreView(Resource):
    """
    Класс жанр
    """
    def get(self, gid):
        """
        Вывод жанра по id
        """
        r = genre_service.get_one(gid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200