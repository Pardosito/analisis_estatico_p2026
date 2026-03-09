"""
File that tests several classes and their integration.
"""

import unittest
from io import StringIO
from unittest.mock import patch

from white_box.book_store import Book, BookStore, main


class TestBook(unittest.TestCase):
    """
    Book unittest class.
    """

    def setUp(self):
        """
        Creates the book properties
        """
        self.title = "title"
        self.author = "author"
        self.price = 9.99
        self.quantity = 5

    def test_book_init(self):
        """
        Checks the book properties.
        """
        book = Book(self.title, self.author, self.price, self.quantity)
        self.assertEqual(book.title, self.title)
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.price, self.price)
        self.assertEqual(book.quantity, self.quantity)

    @patch("builtins.print")
    def test_book_display(self, mock_print):
        """
        Checks the book display function.
        """
        book = Book(self.title, self.author, self.price, self.quantity)
        book.display()
        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 4)
        mock_print.assert_any_call(f"Title: {self.title}")
        mock_print.assert_any_call(f"Author: {self.author}")
        mock_print.assert_any_call(f"Price: ${self.price}")
        mock_print.assert_any_call(f"Quantity: {self.quantity}")
        mock_print.assert_called_with(f"Quantity: {self.quantity}")


class TestBookStore(unittest.TestCase):
    """
    Book store unittest class.
    """

    def test_book_store_init(self):
        """
        Checks the book store properties.
        """
        book_store = BookStore()
        self.assertEqual(book_store.books, [])

    def test_book_store_add_book(self):
        """
        Checks the book store can add a book.
        """
        book_store = BookStore()
        book1 = Book("title1", "author1", 9.99, 5)
        book2 = Book("title2", "author2", 19.99, 3)
        book_store.add_book(book1)
        book_store.add_book(book2)
        self.assertEqual(len(book_store.books), 2)
        self.assertEqual(book_store.books[0], book1)
        self.assertEqual(book_store.books[1], book2)

    def test_book_store_display_books_no_books(self):
        """
        Checks the book store displays no books message.
        """
        book_store = BookStore()
        with patch("builtins.print") as mock_print:
            book_store.display_books()
            mock_print.assert_called_once_with("No books in the store.")

    def test_book_store_display_books_with_books(self):
        """
        Checks the book store can display books.
        """
        book1 = Book("title1", "author1", 9.99, 5)
        book2 = Book("title2", "author2", 19.99, 3)

        book_store = BookStore()
        book_store.add_book(book1)
        book_store.add_book(book2)

        with patch("builtins.print") as mock_print:
            book_store.display_books()
            self.assertTrue(mock_print.called)
            mock_print.assert_any_call("Books available in the store:")
            self.assertEqual(mock_print.call_count, 9)  # 1 for header + 4 per book

    def test_book_store_search_book_no_books(self):
        """
        Checks the book store can search for a book even without books.
        """
        book_store = BookStore()

        with patch("builtins.print") as mock_print:
            book_store.search_book("title1")
            self.assertTrue(mock_print.called)
            mock_print.assert_any_call("No book found with title 'title1'.")

    def test_book_store_search_book_with_books(self):
        """
        Checks the book store can search for a book.
        """
        book1 = Book("title1", "author1", 9.99, 5)
        book2 = Book("title2", "author2", 19.99, 3)

        book_store = BookStore()
        book_store.add_book(book1)
        book_store.add_book(book2)

        with patch("builtins.print") as mock_print:
            book_store.search_book("title1")
            self.assertTrue(mock_print.called)
            mock_print.assert_any_call("Found 1 book(s) with title 'title1':")

            book_store.search_book("nonexistent")
            self.assertTrue(mock_print.called)
            mock_print.assert_any_call("No book found with title 'nonexistent'.")


class TestMain(unittest.TestCase):
    """Class that tests the main function of the original file."""

    @patch("builtins.input", side_effect=["1", "4"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_books_empty(self, mock_stdout):
        """Choice 1 with no books prints the empty store message."""
        main()
        self.assertIn("No books in the store.", mock_stdout.getvalue())

    @patch(
        "builtins.input", side_effect=["3", "Dune", "Frank Herbert", "9.99", "5", "4"]
    )
    @patch("sys.stdout", new_callable=StringIO)
    def test_add_book(self, mock_stdout):
        """Choice 3 adds a book and confirms it was added."""
        main()
        self.assertIn("Book 'Dune' added to the store.", mock_stdout.getvalue())

    @patch(
        "builtins.input",
        side_effect=["3", "Dune", "Frank Herbert", "9.99", "5", "1", "4"],
    )
    @patch("sys.stdout", new_callable=StringIO)
    def test_display_books_after_adding(self, mock_stdout):
        """Choice 1 after adding a book shows that book's details."""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Books available in the store:", output)
        self.assertIn("Dune", output)
        self.assertIn("Frank Herbert", output)

    @patch(
        "builtins.input",
        side_effect=["3", "Dune", "Frank Herbert", "9.99", "5", "2", "Dune", "4"],
    )
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_book_found(self, mock_stdout):
        """Choice 2 finds a book that was previously added."""
        main()
        output = mock_stdout.getvalue()
        self.assertIn("Found 1 book(s) with title 'Dune':", output)

    @patch("builtins.input", side_effect=["2", "Unknown Title", "4"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_book_not_found(self, mock_stdout):
        """Choice 2 reports correctly when no matching book exists."""
        main()
        self.assertIn(
            "No book found with title 'Unknown Title'.", mock_stdout.getvalue()
        )

    @patch("builtins.input", side_effect=["2", "dune", "4"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_search_is_case_insensitive(self):
        """Search with wrong case still finds the book (tests .lower() logic)."""
        with patch("book_store.BookStore.search_book") as mock_search:
            main()
            mock_search.assert_called_once_with("dune")

    @patch("builtins.input", side_effect=["99", "4"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_invalid_choice(self, mock_stdout):
        """An unrecognised menu choice prints the invalid choice message."""
        main()
        self.assertIn("Invalid choice. Please try again.", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["4"])
    @patch("sys.stdout", new_callable=StringIO)
    def test_exit(self, mock_stdout):
        """Choice 4 exits the loop cleanly."""
        main()  # Should not loop forever or raise
        self.assertIn("Exiting...", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
