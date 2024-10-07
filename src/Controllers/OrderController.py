from itertools import count

from src.Models.Orders import *

class OrderController:
    def get(self):
        return Orders.select().execute()

    def add(self,input_count_cliens,input_table_id,input_drink_id,input_food_id,input_shift_id,input_status_id):
        Orders.create(count_cliens = input_count_cliens, table_id = input_table_id, drink_id = input_drink_id, food_id = input_food_id,shift_id = input_shift_id, status_id = input_status_id)

    def update_order_pay(self,id_order):
        Orders.update({Orders.status_id : False}).where(Orders.id == id_order).execute()

    def update_order_cooking(self, id_order):
        Orders.update({Orders.status_id : False}).where(Orders.id == id_order).execute()

    def update_order_ready(self,id_order):
        Orders.update({Orders.status_id : False}).where(Orders.id == id_order)
if __name__ == "__main__":
    sh = OrderController()
    for row in sh.get():
        print(row.id)
    print("---------------")
    sh.add(1,1,1,1,1,1)