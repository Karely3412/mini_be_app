import uuid
from sqlalchemy.dialects.postgresql import UUID
import marshmallow as ma

from db import db



class Imessages(db.Model):
    __tablename__ = "Imessages"

    message_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message = db.Column(db.String(), nullable=False)

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.users_id"), nullable=False)

    def __init__(self, message):
        self.message = message


class ImessagesSchema(ma.Schema):
    class Meta:
        fields = ['message_id', 'user_id', 'message']

    
imessage_schema = ImessagesSchema()
imessages_schema = ImessagesSchema(many=True)


