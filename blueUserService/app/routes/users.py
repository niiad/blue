from flask import request
from flask_restplus import Resource, Namespace
from app import crud
from app.schema import user, user_create, profile
from app.database import database

api = Namespace("users", description="User related operations")


@api.route("/")
class UserList(Resource):

    @api.marshal_list_with(user)
    def get(self):
        return crud.get_all_users()

    @api.expect(user_create)
    @api.marshal_with(user, code=201)
    def post(self):
        data = request.json

        if crud.get_user_by_email(data["email"]):
            api.abort(400, "Email already registered!")

        return crud.create_user(data), 201


@api.route("/<int:user_id>")
@api.response(404, "User not found")
class User(Resource):

    @api.marshal_with(user)
    def get(self, user_id):
        fetched_user = crud.get_user(user_id)

        if fetched_user is None:
            api.abort(404, "User not found")

        return fetched_user


@api.route("/<int:user_id>/profile")
@api.response(404, "User not found")
class UserProfile(Resource):

    @api.expect(profile)
    @api.marshal_with(profile, code=201)
    def post(self, user_id):
        fetched_user = crud.get_user(user_id)

        if not fetched_user:
            api.abort(404, "User not found")

        data = request.json

        return crud.create_profile(user_id, data), 201

    @api.expect(profile)
    @api.marshal_with(profile, code=200)
    def put(self, user_id):
        fetched_user = crud.get_user(user_id)

        if not user:
            api.abort(404, "User not found")

        data = request.json

        return crud.update_profile(user_id, data)
