import uuid
from sqlalchemy.dialects.postgresql import UUID 
import marshmallow as ma

from db import db


class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    phone_numb = db.Column(db.String(), nullable=False)


    def __init__(self, name, email, phone_numb):
        self.name = name,
        self.email = email,
        self.phone_numb = phone_numb

    
class UsersSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'name', 'email', 'phone_numb']


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

