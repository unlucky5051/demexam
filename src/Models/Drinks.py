from src.Models.Base import *

class Drinks(Base):
    id = PrimaryKeyField()
    role = CharField()