#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        # Initialize internal variables first
        self._discount = 0
        self.total = 0
        self.items = []
        self.previous_transactions = []

        # Use the setter property to validate the initial discount
        self.discount = discount

    @property
    def discount(self):
        """Getter for discount property."""
        return self._discount

    @discount.setter
    def discount(self, value):
        """Setter for discount that enforces type and range rules."""
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity=1):
        """Adds price to total, appends item(s), and logs transaction history."""
        # Add price * quantity to the total
        self.total += price * quantity

        # Add the item to the items list quantity times
        for _ in range(quantity):
            self.items.append(item)

        # Add transaction tracking dictionary object
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity,
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        """Applies the discount percentage to the total register price.

        Prints a success message when a discount is applied, otherwise
        prints that there is no discount to apply.
        """
        if self.discount and self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount

            # Format total without unnecessary .0 when it's a whole number
            if isinstance(self.total, float) and self.total.is_integer():
                total_display = int(self.total)
            elif isinstance(self.total, int):
                total_display = self.total
            else:
                total_display = round(self.total, 2)

            print(f"After the discount, the total comes to ${total_display}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Undoes the last transaction, correcting total, items, and history."""
        # Ensure there are transactions in the array to void
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Remove the last transaction from previous_transactions
        last_tx = self.previous_transactions.pop()

        # Deduct the cost from the total
        tx_cost = last_tx["price"] * last_tx["quantity"]
        self.total -= tx_cost

        # Remove the item from the items list as many times as its quantity
        for _ in range(last_tx["quantity"]):
            if last_tx["item"] in self.items:
                self.items.remove(last_tx["item"])
