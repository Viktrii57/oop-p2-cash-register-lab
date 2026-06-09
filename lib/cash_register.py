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

    def add_item(self, item, price, quantity):
        """Adds price to total, appends item, and logs transaction history."""
        # Add price * quantity to the total
        self.total += price * quantity
        
        # Add the item to the items array
        self.items.append(item)
        
        # Add transaction tracking dictionary object
        transaction = {
            "item": item,
            "price": price,
            "quantity": quantity
        }
        self.previous_transactions.append(transaction)

    def apply_discount(self):
        """Applies the discount percentage to the total register price."""
        # Discount is a percentage off of the total price
        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount

    def void_last_transaction(self):
        """Undoes the last transaction, correcting total, items, and history."""
        # Ensure there are transactions in the array to void
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        # Remove the last item from previous_transactions
        last_tx = self.previous_transactions.pop()
        
        # Ensure price reflects correctly by deducting it from the total
        tx_cost = last_tx["price"] * last_tx["quantity"]
        self.total -= tx_cost
        
        # Ensure items reflects correctly by removing the item from the array
        if last_tx["item"] in self.items:
            self.items.remove(last_tx["item"])
