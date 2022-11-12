"""
Cook cook cook, orders all day

As a chef in a restaurant, you cook a bunch of dishes
You can only take one order at a time, and you're tired of having
people complain at you when you don't do their order first. So you decide to
set up a system where you accumulate a "list" of orders and cook one order
-- the first order that was put into the "list" -- at a time.

Your job is to implement this "list" as an OrderQueue.
You should be able to add new orders into your OrderQueue
and remove finished orders from your OrderQueue.
Starter code is provided.
"""


class OrderQueue:
    def __init__(self) -> None:
        self.orders = []

    def dequeue(self) -> str:
        """
        Removes the first order in the OrderQueue
        and returns it
        """
        # your code here
        pass

    def enqueue(self, order: str) -> None:
        """
        Inserts the order into the OrderQueue

        Args:
            order: str - the order to be inserted into the OrderQueue
        """
        # your code here
        pass

    def __len__(self):
        return len(self.orders)


# test code
uncooked_orders = OrderQueue()

# 3 customers ordered at the same time
uncooked_orders.enqueue("a medium rare steak")
uncooked_orders.enqueue("six gyoza")
uncooked_orders.enqueue("two enchiladas")

# now you cook them one by one
for order in range(len(uncooked_orders)):
    # this should print
    # the medium rare steak first, then the gyoza, and finally the enchiladas
    print(f"finished cooking {uncooked_orders.dequeue()}")
print(f"done! (exactly {len(uncooked_orders)} orders left)")
