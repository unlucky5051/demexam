from src.Models.Base import *
from src.Models.Roles import Roles
class Users(Base):
    id = PrimaryKeyField()
    login = CharField()
    password = CharField()
    name = CharField()
    role_id = ForeignKeyField(Roles)
    status = BooleanField(default=1)