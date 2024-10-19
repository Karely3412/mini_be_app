from flask import jsonify
from db import db
from models.imessages import Imessages, imessage_schema, imessages_schema
from util.populate_object import populate_object



def create_imessage(req):
    post_data = req.form if req.form else req.json
    fields = ["message", "user_id"]

    for field in fields:
        if field not in post_data:
            return jsonify({"message": "field required"}), 400

    for field in fields:
        if post_data[field] == "":
            return jsonify({"message": "field required"}), 400

    new_imessage = Imessages.get_new_imessage()
    populate_object(new_imessage, post_data)

    db.session.add(new_imessage)
    db.session.commit()

    return jsonify({"message": "imessage created successfully", "imessage": imessage_schema.dump(new_imessage)}), 200


def get_imessages():
    imessage_get = db.session.query(Imessages).all()

    return jsonify({"message": "imessages found", "results": imessages_schema.dump(imessage_get)}), 200


def get_imessage(message_id):
    imessage_get = db.session.query(Imessages).filter(Imessages.message_id == message_id).first()

    return jsonify({"message": "user found", "result": imessage_schema.dump(imessage_get)}), 200


def update_imessage(req, message_id):
    post_data = req.form if req.form else req.json


    if "message" not in post_data:
        return jsonify({"message": "message not found"})
    
    message_query = db.session.query(Imessages).filter(Imessages.message_id == message_id).first()
    
    populate_object(message_query, post_data)

    db.session.commit()
    return jsonify({"message": "message updated", "result": imessage_schema.dump(message_query)}), 200




def deletle_imessage(message_id):
    user_delete = db.session.query(Imessages).filter(Imessages.message_id == message_id).first()

    db.session.delete(user_delete)
    db.session.commit()

    return jsonify({"messages": "user deleted"}),200












