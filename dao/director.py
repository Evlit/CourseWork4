# DAO Director - режиссеры
from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).filter(Director.id == did).one_or_none()

    def get_all(self):
        return self.session.query(Director).all()

