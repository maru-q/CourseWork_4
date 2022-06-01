import jwt
from flask import request
from flask_restx import Resource, Namespace

import constants
from implemented import user_service
from utils import auth_required, get_token_from_headers

user_ns = Namespace("user")


@user_ns.route("/")
class UsersView(Resource):

    @auth_required
    def get(self):
        token = get_token_from_headers(request.headers)

        decoded_token = jwt.decode(
                        jwt=token,
                        key=constants.SECRET_HERE,
                        algorithms=[constants.JWT_ALGORITHM]
                    )
        email = decoded_token.get("email")

        return user_service.get_user_profile(email), 200

    @auth_required
    def patch(self):
        token = get_token_from_headers(request.headers)

        decoded_token = jwt.decode(
            jwt=token,
            key=constants.SECRET_HERE,
            algorithms=[constants.JWT_ALGORITHM]
        )
        email = decoded_token.get("email")

        user_service.update(email, request.json)
        return "", 204

    @auth_required
    def put(self):
        token = get_token_from_headers(request.headers)

        decoded_token = jwt.decode(
            jwt=token,
            key=constants.SECRET_HERE,
            algorithms=[constants.JWT_ALGORITHM]
        )
        email = decoded_token.get("email")

        user_service.change_password(email, request.json)
        return "", 204
