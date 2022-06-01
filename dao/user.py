from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def create(self, data: dict):

        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return ""

    def get_by_email(self, email):
        return self.session.query(User).filter(User.email == email).first()

    def update(self, email, name, surname, favorite_genre):
        user = self.session.query(User).filter(User.email == email).first()
        user.name = name
        user.surname = surname
        user.favorite_genre = favorite_genre
        self.session.commit()

    def change_password(self, email, new_password):
        user = self.session.query(User).filter(User.email == email).first()
        user.password = new_password
        self.session.commit()
