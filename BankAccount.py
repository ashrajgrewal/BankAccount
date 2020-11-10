#Bank Account Ashraj Grewal CS 1.1
class BankAccount():
    def __init__(self, full_name, account_number, routing_number, balance=0):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:{}")
    def withdraw(self, amount):

    def get_balance():

    def add_interest():

    def print_receipt():
