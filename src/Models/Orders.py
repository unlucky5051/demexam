from src.Models.Base import *
from src.Models.Drinks import Drinks
from src.Models.Foods import Foods
from src.Models.Shifts import Shifts
from src.Models.Statuces import Statuces
from src.Models.Tables import Tables


class Orders(Base):
    id = PrimaryKeyField()
    count_cliens = IntegerField()
    table_id = ForeignKeyField(Tables)
    drink_id = ForeignKeyField(Drinks)
    food_id = ForeignKeyField(Foods)
    shift_id = ForeignKeyField(Shifts)
    status_id = ForeignKeyField(Statuces)
