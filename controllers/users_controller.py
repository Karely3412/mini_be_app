from flask import jsonify
from db import db
from models.users import Users, user_schema, users_schema
from util.populate_object import populate_object

def create_user(req):
    post_data = req.json
    fields = ["name", "email", "phone_numb"]

    for field in fields:
        if field not in post_data:
            return jsonify({"message": "field required"}), 400
        
    for field in fields:
        if post_data[field] == "":
            return jsonify({"message": "field required"}), 400


    new_user = Users.get_new_user()
    populate_object(new_user,post_data)

    db.session.add(new_user)
    db.session.commit()


    return jsonify({"message": "user added successfully", "user": user_schema.dump(new_user)}), 200



def get_users():
    get_all_users = db.session.query(Users).all()

    return jsonify({"message": "users found", "results": users_schema.dump(get_all_users) })


def get_user(user_id):
    get_user_by_id = db.session.query(Users).filter(Users.user_id == user_id).first()

    return jsonify({"message":"user found", "result": user_schema.dump(get_user_by_id)}), 200



def delete_user (user_id):
    user_delete = db.session.query(Users).filter(Users.user_id == user_id).first()

    if not delete_user:
        return jsonify({"message": "user not found"}), 404

    db.session.delete(user_delete)
    db.session.commit()

    return jsonify({"message": "user deleted"}), 200
