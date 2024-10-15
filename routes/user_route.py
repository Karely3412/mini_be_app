from flask import Blueprint, request
from controllers import users_controller

users = Blueprint("users", __name__)

@users.route("/user/create", methods=["POST"])
def create_user():
    return users_controller.create_user(request)

@users.route("/users/get", methods=["GET"])
def get_users():
    return users_controller.get_users()

@users.route("/user/get/<user_id>", methods=["GET"])
def get_user(user_id):
    return users_controller.get_user(user_id)

@users.route("/user/update/<user_id>", methods=["PUT"])
def update_user(user_id):
    return users_controller.test()

@users.route("/user/delete/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    return users_controller.delete_user(user_id)