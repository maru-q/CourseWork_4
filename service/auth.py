from flask_restx import abort

from dao.auth import AuthDAO

from utils import get_hashed_password, generate_tokens, decode_token


class AuthService:
    def __init__(self, dao: AuthDAO):
        self.dao = dao

    def login(self, data: dict):
        user_data = self.dao.get_by_email(data["email"])
        if user_data is None:
            abort(401, message="User not found")
        hashed_password = get_hashed_password(data["password"])
        if user_data["password"] != hashed_password:
            abort(401, message="Invalid password")

        tokens: dict = generate_tokens(
            {
                "email": data["email"]
            }
        )
        return tokens

    def get_new_tokens(self, refresh_token: str):
        decoded_token = decode_token(refresh_token, refresh_token=True)

        tokens = generate_tokens(
            data={
                "email": decoded_token["email"]
            }
        )
        return tokens

    def register(self, data: dict):
        data["password"] = get_hashed_password(data["password"])
        return self.dao.create(data)


