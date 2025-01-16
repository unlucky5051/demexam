from itertools import count

from src.Models.Orders import *

class OrderController:
    def get(self):
        return Orders.select().execute()


    def add(self, count_cliens, table_id, drink_id, food_id, shift_id, status_id):
        Orders.create(
            count_cliens=count_cliens,
            table_id=table_id,
            drink_id=drink_id,
            food_id=food_id,
            shift_id=shift_id,
            status_id=status_id
            )
    def update_order_pay(self,id_order):
        Orders.update({Orders.status_id : False}).where(Orders.id == id_order).execute()

    def update_order_cooking(self, id_order):
        Orders.update({Orders.status_id : False}).where(Orders.id == id_order).execute()

    def update_order_ready(self,id_order):
        Orders.update({Orders.status_id : False}).where(Orders.id == id_order)

    def delete_order(self, order_id):
        order = Orders.get_or_none(Orders.id == order_id)
        if order:
            order.delete_instance()
            return True
        return False

if __name__ == "__main__":
    sh = OrderController()
    for row in sh.get():
        print(row.id)
    print("---------------")
    sh.add(1,1,1,1,1,1)