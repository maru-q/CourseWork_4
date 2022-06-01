from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
from utils import auth_required

director_ns = Namespace("directors")


@director_ns.route("/")
class DirectorsView(Resource):
    @auth_required
    def get(self):
        page = request.args.get("page", type=int, default=None)
        return DirectorSchema(many=True).dump(director_service.get_all(page)), 200


@director_ns.route("/<int:did>")
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        return DirectorSchema().dump(director_service.get_one(did)), 200
