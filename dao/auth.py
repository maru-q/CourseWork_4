from dao.model.user import User, UserSchema

user_schema = UserSchema()


class AuthDAO:
    def __init__(self, session):
        self.session = session

    def get_by_email(self, email):
        return user_schema.dump(self.session.query(User).filter(User.email == email).first())

    def create(self, data):
        new_user = User(**data)
        self.session.add(new_user)
        self.session.commit()
        return new_user
