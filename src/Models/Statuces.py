from src.Models.Base import *

class Statuces(Base):
    id = PrimaryKeyField()
    name = CharField()