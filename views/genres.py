from flask import request
from flask_restx import Resource, Namespace

from dao.model.genres import GenreSchema
from implemented import genre_service
from utils import auth_required

genre_ns = Namespace("genres")


@genre_ns.route("/")
class GenresView(Resource):
    @auth_required
    def get(self):
        page = request.args.get("page", type=int, default=None)
        all_genres = genre_service.get_all(page)
        res = GenreSchema(many=True).dump(all_genres)
        return res, 200


@genre_ns.route("/<int:rid>")
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200



