from flask_restplus import fields
from app.routes.users import api

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
