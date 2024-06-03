from flask import request
from flask_restx import Resource, Namespace, fields

from app import crud

api = Namespace("users", description="User related operations")

user = api.model("User", {
    "id": fields.Integer(readOnly=True, description="The ID of the user"),
    "first_name": fields.String(required=True, description="The first name of the user"),
    "last_name": fields.String(required=True, description="The last name of the user"),
    "username": fields.String(required=True, description="The unique username of the user"),
    "email": fields.String(required=True, description="The email address of the user")
})

user_create = api.model("UserCreate", {
    "username": fields.String(required=True, description="The unique username of the user"),
    "email": fields.String(required=True, description="The email address of the user"),
    "password": fields.String(required=True, description="The password of the user")
})

profile = api.model("Profile", {
    "id": fields.Integer(readOnly=True, description="The ID of the profile"),
    "user_id": fields.Integer(required=True, description="The user ID associated with this profile"),
    "gender": fields.String(description="The gender of the user"),
    "eu_size": fields.Integer(description="The size of the foot of the user in EU measurement scale"),
    "post_address": fields.String(description="The Ghana Post Address of the user"),
    "city": fields.String(description="The city the user is situated"),
    "region": fields.String(description="The region of the user"),
    "country": fields.String(description="The country of the user"),
    "phone": fields.String(description="The phone number of the user")
})


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

        if not fetched_user:
            api.abort(404, "User not found")

        data = request.json

        return crud.update_profile(user_id, data)
