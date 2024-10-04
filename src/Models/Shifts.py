from src.Models.Base import *
from src.Models.Users import Users

class Shifts(Base):
    id = PrimaryKeyField()
    date = DateTimeField()
    cook = ForeignKeyField(Users)
    oficiant_1 = ForeignKeyField(Users)
    oficiant_2 = ForeignKeyField(Users)