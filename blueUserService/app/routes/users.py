from flask import request
from flask_restplus import Resource, Namespace
from app import crud
from app.schema import user, user_create
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
