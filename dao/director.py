from typing import Dict, Any

from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def get_by_page(self, page):
        return self.session.query(Director).paginate(page, 12, False).items

    def create(self, director_data):
        new_director = Director(**director_data)
        self.session.add(new_director)
        self.session.commit()
        return new_director

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, did: int, data: Dict[str, Any]):
        self.session.query(Director).filter(Director.id == did).update(data)
        self.session.commit()
