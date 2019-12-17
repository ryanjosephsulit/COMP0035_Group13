# Author: Oliver Marshall
# Wallet class unit tests Python code:

import unittest

from Wallet.wallet import Wallet


class TestWallet(unittest.TestCase):

    def setUp(self):
        # Create a test Wallet object
        self.test_account = Wallet()

        # Set a test balance to 1000 LangCoins.
        self.test_account.balance = 1000.0

    # Testing that a deposit of 100 to test balance, then a withdrawal of 200 yields expected balance of 900.
    def test_legal_transactions_work(self):
        expected_balance = 900.00
        self.test_account.make_payment(100, 200)
        self.assertEqual(expected_balance, self.test_account.balance)

    # Testing that a long number input for a transaction is rounded to 2 decimal places, suitable for monetary values.
    def test_long_number_is_rounded_to_2_decimal_places(self):
        expected_balance = 999.78
        self.test_account.make_payment(0, 0.2244124)
        # If 0.2244124 is rounded to 2 d.p., it is 0.22, withdrawing this yields the expected balance of 999.78
        self.assertEqual(expected_balance, self.test_account.balance)

    # Testing that the transaction list is updated accordingly.
    def test_transaction_list_works(self):
        expected_transaction_list = [100,-200]
        self.test_account.make_payment(100,200)
        self.assertEqual(expected_transaction_list,self.test_account.transactions)

    # Testing that an input of a negative number for a transaction isn't accepted by the Wallet class.
    def test_negative_numbers_raises_exception(self):
        with self.assertRaises(ValueError):
            self.test_account.make_payment(-5, 0)

    # Testing that withdrawing a number above the current balance isn't accepted by Wallet class.
    def test_withdrawal_bigger_than_balance_raises_exception(self):
        with self.assertRaises(ValueError):
            self.test_account.make_payment(0, 1001)

    # Testing that inputting a non-number (e.g. a word) for a deposit isn't accepted by wallet class
    def test_illegal_deposit_raises_exception(self):
        with self.assertRaises(TypeError):
            self.test_account.make_payment('word', 0)

    # Testing that inputting a non-number (e.g. a word) for a withdrawal isn't accepted by wallet class
    def test_illegal_withdraw_raises_exception(self):
        with self.assertRaises(TypeError):
            self.test_account.make_payment(0, 'word')

