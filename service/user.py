from flask_restx import abort

from dao.user import UserDAO
from utils import get_hashed_password
from dao.model.user import UserSchema

user_schema = UserSchema()


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def register(self, data: dict):
        data["password"] = get_hashed_password(data["password"])
        return self.dao.create(data)

    def update(self, email, data: dict):
        name = data.get("name")
        surname = data.get("surname")
        favorite_genre = data.get("favorite_genre")
        self.dao.update(email, name, surname, favorite_genre)

    def get_user_profile(self, email):
        user_data: dict = user_schema.dump(self.dao.get_by_email(email))
        profile = {
            "user_name": user_data["name"],
            "user_surname": user_data["surname"],
            "favorite_genre": user_data["favorite_genre"]
        }
        return profile

    def change_password(self, email, data: dict):
        user_data = user_schema.dump(self.dao.get_by_email(email))
        hashed_password1 = get_hashed_password(data["password1"])
        if hashed_password1 != user_data["password"]:
            abort(401, message="Invalid password")
        new_password = get_hashed_password(data.get("password2"))

        return self.dao.change_password(email, new_password)




