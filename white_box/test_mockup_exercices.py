"""
Test cases for mock up exercises
"""

import subprocess
import unittest
from unittest.mock import mock_open, patch

from white_box.mockup_exercices import (
    execute_command,
    fetch_data_from_api,
    perform_action_based_on_time,
    read_data_from_file,
)


class TestFetchDataFromApi(unittest.TestCase):
    """
    Fetch data from API unittest class.
    """

    @patch("white_box.mockup_exercices.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"key": "value"}

        result = fetch_data_from_api("https://api.example.com/data")

        self.assertEqual(result, {"key": "value"})

        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)

    @patch("white_box.mockup_exercices.requests.get")
    def test_fetch_data_from_api_not_found(self, mock_get):
        """
        Not Found case
        """

        mock_get.return_value.status_code = 404
        mock_get.return_value.json.return_value = {"Message": "Not Found"}

        result = fetch_data_from_api("https://api.example.com/data")

        self.assertEqual(result, {"Message": "Not Found"})

        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)

    @patch("white_box.mockup_exercices.requests.get")
    def test_fetch_data_from_api_bad_request(self, mock_get):
        """
        Not Found case
        """

        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {"Message": "Bad Request"}

        result = fetch_data_from_api("https://api.example.com/data")

        self.assertEqual(result, {"Message": "Bad Request"})

        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)

    @patch("white_box.mockup_exercices.requests.get")
    def test_fetch_data_from_api_forbidden(self, mock_get):
        """
        Not Found case
        """

        mock_get.return_value.status_code = 403
        mock_get.return_value.json.return_value = {"Message": "Forbidden"}

        result = fetch_data_from_api("https://api.example.com/data")

        self.assertEqual(result, {"Message": "Forbidden"})

        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)


class TestReadDataFromFile(unittest.TestCase):
    """
    Read data from file unittest class
    """

    @patch("builtins.open", new_callable=mock_open, read_data="Data read succesfully")
    def test_read_data_from_file_success(self, mocked_open):
        """
        Succesful case
        """

        result = read_data_from_file("example.txt")
        self.assertEqual(result, "Data read succesfully")
        mocked_open.assert_called_once_with("example.txt", encoding="utf-8")

    @patch("builtins.open", side_effect=FileNotFoundError("No such file"))
    def test_read_data_from_file_failure(self, mocked_open):
        """
        Failure case
        """

        with self.assertRaises(FileNotFoundError):
            read_data_from_file("example.txt")

        mocked_open.assert_called_once_with("example.txt", encoding="utf-8")


class TestExecuteCommand(unittest.TestCase):
    """
    Execute command unittest class
    """

    @patch("subprocess.run")
    def test_execute_command_success(self, mock_run):
        """
        Succesful case
        """

        mock_run.return_value = subprocess.CompletedProcess(
            args=["mock", "arg"], stdout="Mock output", returncode=0
        )

        result = execute_command(["mock", "arg"])
        self.assertEqual(result, "Mock output")
        mock_run.assert_called_once_with(
            ["mock", "arg"], capture_output=True, check=False, text=True
        )

    @patch(
        "subprocess.run",
        side_effect=subprocess.CalledProcessError(
            returncode=1, cmd=["mock", "arg"], output="", stderr="failure"
        ),
    )
    def test_execute_command_failure(self, mock_run):
        """
        Failure case
        """

        with self.assertRaises(subprocess.CalledProcessError):
            execute_command(["mock", "arg"])
        mock_run.assert_called_once_with(
            ["mock", "arg"], capture_output=True, check=False, text=True
        )


class TestPerformActionBasedOnTime(unittest.TestCase):
    """
    Perform action based on time unittest class
    """

    @patch("time.time", return_value=5)
    def test_perform_action_based_on_time_a(self, mock_time):
        """
        Test action A execution when time is less than 10.
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action A")
        mock_time.assert_called_once_with()

    @patch("time.time", return_value=15)
    def test_perform_action_based_on_time_b(self, mock_time):
        """
        Test action B execution when time is greater than 10.
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")
        mock_time.assert_called_once_with()

    @patch("time.time", return_value=10)
    def test_perform_action_based_on_time_limit(self, mock_time):
        """
        Test action B execution when time is exactly at the limit of 10.
        """
        result = perform_action_based_on_time()
        self.assertEqual(result, "Action B")
        mock_time.assert_called_once_with()
