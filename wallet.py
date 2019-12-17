# Author: Oliver Marshall
# This is the Python 3.0 Code for the 'Wallet' class found in the class diagram
# for the proposed software engineering design of the web-app 'LangBridge'.


class Wallet:

    def __init__(self):
        self.balance = 0  # The user's balance of the virtual in-app currency 'LangCoin'.
        self.transactions = []  # A list of user transactions.

    def make_payment(self, deposit, withdraw):  # Withdraw/Deposit LangCoins function
        try:
            # Deposit LangCoin code:
            if deposit >= 0:
                new_deposit = float(
                    "{:.2f}".format(deposit))  # Rounding user input to a 2 decimal point number, suitable for money.
                self.balance += new_deposit  # Updating balance
                if deposit > 0:
                    self.transactions.append(+new_deposit)  # Adding this to the transaction history list
            else:
                raise ValueError
            # Withdraw LangCoin code:
            if withdraw >= 0:
                new_withdraw = float(
                    "{:.2f}".format(withdraw))  # Rounding user input to a 2 decimal point number, suitable for money.
                if self.balance >= new_withdraw:  # If user has enough in their balance to withdraw the inputted amount
                    self.balance -= new_withdraw  # Updating balance
                    if withdraw > 0:
                        self.transactions.append(-new_withdraw)  # Adding this to the transaction history list
                    return self.balance
                else:
                    raise ValueError
            else:
                raise ValueError

        except TypeError:  # If the user doesn't input a number.
            raise TypeError


# Creating an object of 'Wallet' class
s = Wallet()

# Calling the function
s.make_payment(0, 0)

