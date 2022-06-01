from typing import Dict, Any

from dao.director import DirectorDAO
from dao.model.director import DirectorSchema

director_schema = DirectorSchema()


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self, page):
        if page is not None:
            return self.dao.get_by_page(page)
        return self.dao.get_all()

    def create(self, director_data):
        return director_schema.dump(self.dao.create(director_data))

    def update(self, did, data: Dict[str, Any]):
        self.dao.update(did, director_schema.load(data))

    def delete(self, did):
        self.dao.delete(did)