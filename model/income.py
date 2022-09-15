from marshmallow import post_load
from .transaction import Transaction, TransactionSchema
from .transaction_type import TransactionType

class Expense(Transaction):
    def __init__(self, description, amount):
        super(Expense, self).__init__(description, -abs(amount), TransactionType.EXPENSE)
