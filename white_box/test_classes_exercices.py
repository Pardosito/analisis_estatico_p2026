"""Unit tests for state machine exercise classes.

This module contains test cases for all state machine classes
including vending machines, traffic lights, user authentication, document
editing systems, and elevator systems.
"""

import unittest

from white_box.classes_exercices import (
    DocumentEditingSystem,
    ElevatorSystem,
    TrafficLight,
    UserAuthentication,
    VendingMachine,
)


class TestVendingMachine(unittest.TestCase):
    """Tests for the Vending Machine class"""

    def setUp(self):
        self.vending_machine = VendingMachine()
        self.assertEqual(self.vending_machine.state, "Ready")

    def test_insert_coin_status_ready(self):
        """Using status 'Ready' to test the function"""
        self.assertEqual(
            self.vending_machine.insert_coin(), "Coin Inserted. Select your drink."
        )
        self.assertEqual(self.vending_machine.state, "Dispensing")

    def test_insert_coin_status_dispensing(self):
        """Using status 'Dispensing' to test the function"""
        self.vending_machine.state = "Dispensing"
        self.assertEqual(
            self.vending_machine.insert_coin(), "Invalid operation in current state."
        )

    def test_inset_coin_status_other(self):
        """Using a different status to test the function"""
        self.vending_machine.state = "Other"
        self.assertEqual(
            self.vending_machine.insert_coin(), "Invalid operation in current state."
        )

    def test_select_drink_status_dispensing(self):
        """Using status 'Dispensing' to test the function"""
        self.vending_machine.state = "Dispensing"
        self.assertEqual(
            self.vending_machine.select_drink(), "Drink Dispensed. Thank you!"
        )
        self.assertEqual(self.vending_machine.state, "Ready")

    def test_select_drink_status_ready(self):
        """Using status 'Ready' to test the function"""
        self.assertEqual(
            self.vending_machine.select_drink(), "Invalid operation in current state."
        )

    def test_select_drink_status_other(self):
        """Using other status to test the function"""
        self.vending_machine.state = "Other"
        self.assertEqual(
            self.vending_machine.select_drink(), "Invalid operation in current state."
        )


class TestTrafficLight(unittest.TestCase):
    """Tests for the traffic_light class"""

    def setUp(self):
        self.traffic_light = TrafficLight()
        self.assertEqual(self.traffic_light.state, "Red")

    def test_change_state_from_red(self):
        """Changing light from Red"""
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Green")

    def test_change_state_from_green(self):
        """Changing light from Green"""
        self.traffic_light.state = "Green"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Yellow")

    def test_change_state_from_yellow(self):
        """Changing light from Yellow"""
        self.traffic_light.state = "Yellow"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.state, "Red")

    def test_get_current_state_from_red(self):
        """Getting current state from Red"""
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_get_current_state_from_green(self):
        """Getting current state from Green"""
        self.traffic_light.state = "Green"
        self.assertEqual(self.traffic_light.get_current_state(), "Green")

    def test_get_current_state_from_yellow(self):
        """Getting current state from Yellow"""
        self.traffic_light.state = "Yellow"
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")


class TestUserAuthentication(unittest.TestCase):
    """Tests for the User Authentication class"""

    def setUp(self):
        self.user_authentication = UserAuthentication()
        self.assertEqual(self.user_authentication.state, "Logged Out")

    def test_login_state_in(self):
        """Testing login state with logged in"""
        self.assertEqual(self.user_authentication.login(), "Login successful")
        self.assertEqual(self.user_authentication.state, "Logged In")

    def test_login_state_out(self):
        """Testing login state with logged out"""
        self.user_authentication.state = "Logged In"
        self.assertEqual(
            self.user_authentication.login(), "Invalid operation in current state"
        )
        self.assertEqual(self.user_authentication.state, "Logged In")

    def test_logout_state_in(self):
        """Testing login state with logged in"""
        self.user_authentication.state = "Logged In"
        self.assertEqual(self.user_authentication.logout(), "Logout successful")
        self.assertEqual(self.user_authentication.state, "Logged Out")

    def test_logout_state_out(self):
        """Testing login state with logged out"""
        self.assertEqual(
            self.user_authentication.logout(), "Invalid operation in current state"
        )
        self.assertEqual(self.user_authentication.state, "Logged Out")


class TestDocumentEditingSysten(unittest.TestCase):
    """Tests for the document_editing_system class"""

    def setUp(self):
        self.document_editing_system = DocumentEditingSystem()
        self.assertEqual(self.document_editing_system.state, "Editing")

    def test_save_document_state_editing(self):
        """Testing saving document from editing state"""
        self.assertEqual(
            self.document_editing_system.save_document(), "Document saved successfully"
        )
        self.assertEqual(self.document_editing_system.state, "Saved")

    def test_save_document_state_saved(self):
        """Testing saving document from saved state"""
        self.document_editing_system.state = "Saved"
        self.assertEqual(
            self.document_editing_system.save_document(),
            "Invalid operation in current state",
        )
        self.assertEqual(self.document_editing_system.state, "Saved")

    def test_edit_document_state_saved(self):
        """Testing editing document from saved state"""
        self.document_editing_system.state = "Saved"
        self.assertEqual(
            self.document_editing_system.edit_document(), "Editing resumed"
        )
        self.assertEqual(self.document_editing_system.state, "Editing")

    def test_edit_document_state_editin(self):
        """Testing editing document from editing state"""
        self.document_editing_system.state = "Editing"
        self.assertEqual(
            self.document_editing_system.edit_document(),
            "Invalid operation in current state",
        )
        self.assertEqual(self.document_editing_system.state, "Editing")


class TestElevatorSystem(unittest.TestCase):
    """Test for the Elevator System class"""

    def setUp(self):
        self.elevator_system = ElevatorSystem()
        self.assertEqual(self.elevator_system.state, "Idle")

    def test_move_up_state_idle(self):
        """Testing moving up from idle state"""
        self.assertEqual(self.elevator_system.move_up(), "Elevator moving up")
        self.assertEqual(self.elevator_system.state, "Moving Up")

    def test_move_up_state_up(self):
        """Testing moving up from moving up state"""
        self.elevator_system.state = "Moving Up"
        self.assertEqual(
            self.elevator_system.move_up(), "Invalid operation in current state"
        )
        self.assertEqual(self.elevator_system.state, "Moving Up")

    def test_move_up_state_down(self):
        """Testing moving up from moving down state"""
        self.elevator_system.state = "Moving Down"
        self.assertEqual(
            self.elevator_system.move_up(), "Invalid operation in current state"
        )
        self.assertEqual(self.elevator_system.state, "Moving Down")

    def test_move_down_state_idle(self):
        """Testing moving down from idle state"""
        self.elevator_system.state = "Idle"
        self.assertEqual(self.elevator_system.move_down(), "Elevator moving down")
        self.assertEqual(self.elevator_system.state, "Moving Down")

    def test_move_down_state_up(self):
        """Testing moving down from moving up state"""
        self.elevator_system.state = "Moving Up"
        self.assertEqual(
            self.elevator_system.move_down(), "Invalid operation in current state"
        )
        self.assertEqual(self.elevator_system.state, "Moving Up")

    def test_move_down_state_down(self):
        """Testing moving down from moving down state"""
        self.elevator_system.state = "Moving Down"
        self.assertEqual(
            self.elevator_system.move_down(), "Invalid operation in current state"
        )
        self.assertEqual(self.elevator_system.state, "Moving Down")

    def test_stop_state_idle(self):
        """Testing stopping from state idle"""
        self.elevator_system.state = "Idle"
        self.assertEqual(
            self.elevator_system.stop(), "Invalid operation in current state"
        )
        self.assertEqual(self.elevator_system.state, "Idle")

    def test_stop_state_up(self):
        """Testing stopping from moving up state"""
        self.elevator_system.state = "Moving Up"
        self.assertEqual(self.elevator_system.stop(), "Elevator stopped")
        self.assertEqual(self.elevator_system.state, "Idle")

    def test_stop_state_down(self):
        """Testing stopping from moving down state"""
        self.elevator_system.state = "Moving Down"
        self.assertEqual(self.elevator_system.stop(), "Elevator stopped")
        self.assertEqual(self.elevator_system.state, "Idle")
