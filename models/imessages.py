import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db



class Imessages(db.Model):
    __tablename__ = "Imessages"

    message_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Users.users_id"), nullable=False)

    print("Printing iMessages")