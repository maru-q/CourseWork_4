from dao.model.genres import Genre, GenreSchema



class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, bid):
        return self.session.query(Genre).get(bid)

    def get_by_page(self, page):
        return self.session.query(Genre).paginate(page, 12, False).items

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_d):
        ent = Genre(**genre_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, rid):
        genre = self.get_one(rid)
        self.session.delete(genre)
        self.session.commit()

    def update(self, rid, genre_d):
        self.session.query(Genre).filter(Genre.id == rid).update(genre_d)
        self.session.commit()
