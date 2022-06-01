from flask import request
from flask_restx import Resource, Namespace
from flask_paginate import Pagination

from dao.model.movie import MovieSchema
from implemented import movie_service
from utils import auth_required, admin_required

movie_ns = Namespace("movies")


@movie_ns.route("/")
class MoviesView(Resource):
    @auth_required
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        page = request.args.get("page", type=int, default=None)
        status = request.args.get("status")
        filters = {
            "director_id": director,
            "genre_id": genre,
            "year": year,
            "status": status,
            "page": page
        }
        all_movies = movie_service.get_all(filters)

        res = MovieSchema(many=True).dump(all_movies)
        return res, 200


@movie_ns.route("/<int:bid>")
class MovieView(Resource):
    @auth_required
    def get(self, bid):
        b = movie_service.get_one(bid)
        sm_d = MovieSchema().dump(b)
        return sm_d, 200
