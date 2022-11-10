# Представление для режиссеров
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service


director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    """
    Класс режиссеров
    """
#    @auth_required
    def get(self):
        """
        Вывод всех режиссеров
        """
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    """
    Класс режиссер
    """
#    @auth_required
    def get(self, did):
        """
        Вывод режиссера по id
        """
        r = director_service.get_one(did)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
