from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genre')


@genre_ns.route('/<int:gid>')
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
