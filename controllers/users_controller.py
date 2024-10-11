from flask import Flask, jsonify
from db import db
from models.users import Users
from util.populate_object import populate_object

def create_user(req):
    post_data = req.json

    return jsonify({"message": "data_retrieved", "results": post_data}), 200

# def get_users():
#     get_all_users = db.session.query(Users).filter(Users.user_id == user_id).first()
