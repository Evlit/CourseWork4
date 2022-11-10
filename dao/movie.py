# DAO Movies - фильмы
from constants import ITEMS_PER_PAGE
from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).filter(Movie.id == mid).one_or_none()

    def get_all(self, filters):
        movie_q = self.session.query(Movie)
        status = filters.get("status")
        page = filters.get("page")
        if status and status == 'new':
            movie_q = movie_q.order_by(Movie.year.desc())

        if page > 0:
            limit = ITEMS_PER_PAGE
            offset = (page - 1) * limit
            movie_q = movie_q.limit(limit).offset(offset)

        return movie_q.all()
