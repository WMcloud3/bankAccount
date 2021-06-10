class BankAccount:
    bank_name = "Ninja Savings and Loans"
    def __init__(self, int_rate = 0.02, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance - amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance - 5
    def display_account_info(self):
        print(self.balance)
    def yield_interest(self):
        if self.balance > 0:
            int_yeld = self.balance * self.int_rate
            self.balance = self.balance + int_yeld




# class BankAccount:
#     
#     def __init__(self, int_rate, balance):
#         # your code here! (remember, instance attributes go here)
#         # don't worry about user info here; we'll involve the User class soon
#     def deposit(self, amount):
#         # your code here - increases the account balance by the given amount
#     def withdraw(self, amount):
#         # your code here - decreases the account balance by the given amount
#         # if there are sufficient funds; if there is not enough money,
#         # print a message "Insufficient funds: Charging a $5 fee" and deduct $5
#     def display_account_info(self):
#         # your code here - print to the console: eg. "Balance: $100"
#     def yield_interest(self):
#         # your code here - increases the account balance by the current balance * the interest rate
#         # (as long as the balance is positive)
