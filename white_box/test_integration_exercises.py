"""Integration test cases for banking and shopping cart exercises."""

import unittest
from unittest.mock import patch

from integration_exercises import (  # pylint: disable=import-error
    BankAccount,
    BankingSystem,
    Product,
    ShoppingCart,
)


class TestBankAccount(unittest.TestCase):
    """Test cases for Bank Account class"""

    def setUp(self):
        account_number = 12345
        balance = 2500
        self.bank_account = BankAccount(account_number, balance)
        self.assertEqual(self.bank_account.account_number, account_number)
        self.assertEqual(self.bank_account.balance, balance)

    @patch("builtins.print")
    def test_view_account(self, mock_print):
        """Test view account displays correct information."""
        self.bank_account.view_account()
        expected_msg = (
            f"The account {self.bank_account.account_number} "
            f"has a balance of {self.bank_account.balance}"
        )
        mock_print.assert_called_with(expected_msg)


class TestBankingSystem(unittest.TestCase):
    """Testing Banking System class"""

    def setUp(self):
        self.banking_system = BankingSystem()
        self.assertDictEqual(self.banking_system.users, {"user123": "pass123"})
        self.assertSetEqual(self.banking_system.logged_in_users, set())

    @patch("builtins.print")
    def test_authenticate(self, mock_print):
        """Test successful user authentication."""
        user = "user123"
        password = "pass123"
        self.assertEqual(self.banking_system.authenticate(user, password), True)
        mock_print.assert_called_with(f"User {user} authenticated successfully.")

    @patch("builtins.print")
    def test_authenticate_failure(self, mock_print):
        """Test failed user authentication."""
        user = "ian"
        password = "12345"
        self.assertEqual(self.banking_system.authenticate(user, password), False)
        mock_print.assert_called_with("Authentication failed.")

    @patch("builtins.print")
    def test_transfer_money_auth_regular_balance(self, mock_print):
        """Test successful money transfer with regular transaction type."""
        user = "user123"
        password = "pass123"
        receiver = "ian"
        amount = 250
        transaction_type = "regular"
        self.banking_system.authenticate(user, password)
        self.assertEqual(
            self.banking_system.transfer_money(
                user, receiver, amount, transaction_type
            ),
            True,
        )

        mock_print.assert_called_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {user} to {receiver} processed successfully."
        )

    @patch("builtins.print")
    def test_transfer_money_auth_express_balance(self, mock_print):
        """Test successful money transfer with express transaction type."""
        user = "user123"
        password = "pass123"
        receiver = "ian"
        amount = 250
        transaction_type = "express"
        self.banking_system.authenticate(user, password)
        self.assertEqual(
            self.banking_system.transfer_money(
                user, receiver, amount, transaction_type
            ),
            True,
        )

        mock_print.assert_called_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {user} to {receiver} processed successfully."
        )

    @patch("builtins.print")
    def test_transfer_money_auth_scheduled_balance(self, mock_print):
        """Test successful money transfer with scheduled transaction type."""
        user = "user123"
        password = "pass123"
        receiver = "ian"
        amount = 250
        transaction_type = "scheduled"
        self.banking_system.authenticate(user, password)
        self.assertEqual(
            self.banking_system.transfer_money(
                user, receiver, amount, transaction_type
            ),
            True,
        )

        mock_print.assert_called_with(
            f"Money transfer of ${amount} ({transaction_type} transfer)"
            f" from {user} to {receiver} processed successfully."
        )

    @patch("builtins.print")
    def test_transfer_money_auth_invalid_type(self, mock_print):
        """Test money transfer with invalid transaction type."""
        user = "user123"
        password = "pass123"
        receiver = "ian"
        amount = 250
        transaction_type = "other"
        self.banking_system.authenticate(user, password)
        self.assertEqual(
            self.banking_system.transfer_money(
                user, receiver, amount, transaction_type
            ),
            False,
        )

        mock_print.assert_called_with("Invalid transaction type.")

    @patch("builtins.print")
    def test_transfer_money_auth_valid_type_insufficient(self, mock_print):
        """Test money transfer with insufficient funds."""
        user = "user123"
        password = "pass123"
        receiver = "ian"
        amount = 1500
        transaction_type = "regular"
        self.banking_system.authenticate(user, password)
        self.assertEqual(
            self.banking_system.transfer_money(
                user, receiver, amount, transaction_type
            ),
            False,
        )

        mock_print.assert_called_with("Insufficient funds.")


class TestProduct(unittest.TestCase):
    """Test cases for Product class."""

    def setUp(self):
        name = "Test Product"
        price = 1500
        self.product = Product(name, price)
        self.assertEqual(self.product.name, name)
        self.assertEqual(self.product.price, price)

    @patch("builtins.print")
    def test_view_product(self, mock_print):
        """Test view product displays correct information."""
        expected_msg = (
            f"The product {self.product.name} has a price of {self.product.price}"
        )
        self.assertEqual(self.product.view_product(), expected_msg)
        mock_print.assert_any_call(expected_msg)


class TestShoppingCart(unittest.TestCase):
    """Test cases for ShoppingCart class."""

    def setUp(self):
        self.shopping_cart = ShoppingCart()
        self.assertListEqual(self.shopping_cart.items, [])
        self.assertEqual(len(self.shopping_cart.items), 0)

    def test_add_product_new(self):
        """Test adding a new product to the cart."""
        product = "Test Product"
        quantity = 1
        self.shopping_cart.add_product(product, quantity)
        added_product = {"product": product, "quantity": quantity}
        self.assertEqual(added_product in self.shopping_cart.items, True)

    def test_add_product_exisiting(self):
        """Test adding an existing product increases quantity."""
        product = "Existing product"
        quantity = 2
        self.shopping_cart.add_product(product, quantity)
        self.shopping_cart.add_product(product)
        added_product = {"product": product, "quantity": quantity + 1}
        self.assertEqual(added_product in self.shopping_cart.items, True)

    def test_remove_product_entirely(self):
        """Test removing a product completely from the cart."""
        product = "Test Product"
        quantity = 1
        added_product = {"product": product, "quantity": quantity}
        self.shopping_cart.add_product(product, quantity)
        self.assertEqual(added_product in self.shopping_cart.items, True)
        self.shopping_cart.remove_product(product, quantity)
        self.assertEqual(added_product in self.shopping_cart.items, False)

    def test_remove_product_partially(self):
        """Test removing part of product quantity from the cart."""
        product = "Test Product"
        quantity = 5
        added_product = {"product": product, "quantity": quantity}
        self.shopping_cart.add_product(product, quantity)
        self.assertEqual(added_product in self.shopping_cart.items, True)
        self.shopping_cart.remove_product(product)
        added_product = {"product": product, "quantity": quantity - 1}
        self.assertEqual(added_product in self.shopping_cart.items, True)

    @patch("builtins.print")
    def test_view_cart(self, mock_print):
        """Test viewing cart displays product information."""
        product = Product("Product 1", 500)
        quantity = 2
        self.shopping_cart.add_product(product, quantity)
        self.shopping_cart.view_cart()
        mock_print.assert_any_call(
            f"{quantity} x {product.name}" f" - ${product.price * quantity}"
        )

    @patch("builtins.print")
    def test_checkout(self, mock_print):
        """Test checkout displays total and completion message."""
        product1 = Product("Product 1", 500)
        product2 = Product("Product 2", 300)
        self.shopping_cart.add_product(product1, 2)
        self.shopping_cart.add_product(product2, 3)
        total = (product1.price * 2) + (product2.price * 3)
        self.shopping_cart.checkout()
        mock_print.assert_any_call(f"Total: ${total}")
        mock_print.assert_any_call("Checkout completed. Thank you for shopping!")
