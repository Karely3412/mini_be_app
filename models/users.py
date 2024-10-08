import uuid
from sqlalchemy.dialects.postgresql import UUID 

from db import db




class Users(db.Model):
    __tablename__ = "Users"

    users_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    print("Printing user")

