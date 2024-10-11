from flask import Blueprint
from controllers import imessages_controller

imessages = Blueprint("imessages", __name__)


@imessages.route("/imessage/create", methods=['POST'])
def create_imessage():
    return imessages_controller.test()

@imessages.route("/imessages/get", methods=["GET"])
def get_imessages():
    return imessages_controller.test()

@imessages.route("/imessage/get/<imessage_id>", methods=["GET"])
def get_imessage(imessage_id):
    return imessages_controller.test()

@imessages.route("/imessage/update/<imessage_id>", methods=["PUT"])
def update_imessage(imessage_id):
    return imessages_controller.test()

@imessages.route("/imessage/delete/<imessage_id>", methods=["DELETE"])
def delete_imessage(imessage_id):
    return imessages_controller.test()