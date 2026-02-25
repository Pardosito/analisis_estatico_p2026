# -*- coding: utf-8 -*-

"""
White-box unit testing examples.
"""
import unittest

from class_exercices import (
    authenticate_user,
    calculate_items_shipping_cost,
    calculate_order_total,
    calculate_quantity_discount,
    calculate_shipping_cost,
    calculate_total_discount,
    categorize_product,
    celsius_to_fahrenheit,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    check_number_status,
    get_weather_advisory,
    grade_quiz,
    validate_credit_card,
    validate_date,
    validate_email,
    validate_login,
    validate_password,
    validate_url,
    verify_age,
)


class TestCheckNumberStatus(unittest.TestCase):
    """Tests for the check_number_status function."""

    def test_check_number_status_positive(self):
        """Checks if a number is positive."""
        self.assertIs(check_number_status(5), "Positive")

    def test_check_number_status_negative(self):
        """Checks if a number is negative."""
        self.assertIs(check_number_status(-5), "Negative")

    def test_check_number_status_zero(self):
        """Checks if a number is zero."""
        self.assertIs(check_number_status(0), "Zero")


class TestValidatePassword(unittest.TestCase):
    """Tests for the validate_password function."""

    def test_validate_password_length_false(self):
        """Checks for invalid password lenght"""
        self.assertIs(validate_password("1234567"), False)

    def test_validate_password_length_true(self):
        """Checks for valid password length (Assumed correctness for rest of criteria)"""
        self.assertIs(validate_password("holA1!asd"), True)

    def test_validate_password_no_uppercase(self):
        """Checks password for missing uppercase character"""
        self.assertIs(validate_password("ahol1!ds3"), False)

    def test_validate_password_no_lowercase(self):
        """Checks password for missing lowercase character"""
        self.assertIs(validate_password("ASDF12!KDD"), False)

    def test_validate_password_no_digit(self):
        """Checks password for missing digit character."""
        self.assertIs(validate_password("ASDFASDF!!"), False)

    def test_validate_password_special_character_1(self):
        """Checks password for special character !"""
        self.assertIs(validate_password("ASbv1!kdd"), True)

    def test_validate_password_special_character_2(self):
        """Checks password for special character @"""
        self.assertIs(validate_password("ASsdf123@"), True)

    def test_validate_password_special_character_3(self):
        """Checks password for special character #"""
        self.assertIs(validate_password("SJKLdslkajf123#"), True)

    def test_validate_password_special_character_4(self):
        """Checks password for special character $"""
        self.assertIs(validate_password("KAJSDmcds$123"), True)

    def test_validate_password_special_character_5(self):
        """Checks password for special character %"""
        self.assertIs(validate_password("ASnvd32%123"), True)

    def test_validate_password_special_character_6(self):
        """Checks password for special character &"""
        self.assertIs(validate_password("AS1dnd3&as2"), True)

    def test_validate_password_complete(self):
        """Checks for valid password"""
        self.assertIs(validate_password("adfnASD134#"), True)


class TestCalculateTotalDiscount(unittest.TestCase):
    """Tests for the calculate_total_discount function."""

    def test_calculate_total_discount_below_limit(self):
        """Checks for correct discount amount below the minimum total"""
        self.assertEqual(calculate_total_discount(99), 0)

    def test_calculate_total_discount_lower_limit(self):
        """Checks for correct discount amount with the lower limit amount"""
        self.assertEqual(calculate_total_discount(100), (0.1 * 100))

    def test_calculate_total_discount_upper_limit(self):
        """Checks for correct discount amount with the upper limit amount"""
        self.assertEqual(calculate_total_discount(500), (0.1 * 500))

    def test_calculate_total_discount_above_limit(self):
        """Checks for correct discount amount with amount above limit"""
        self.assertEqual(calculate_total_discount(501), (0.2 * 501))


class TestCalculateOrderTotal(unittest.TestCase):
    """Tests for the calculate_order_total function."""

    def test_calculate_order_total_single_item_no_discount(self):
        """Checks order total for single item with quantity 1-5 (no discount)"""
        items = [{"quantity": 3, "price": 10}]
        self.assertEqual(calculate_order_total(items), 30)

    def test_calculate_order_total_single_item_5_percent_discount(self):
        """Checks order total for single item with quantity 6-10 (5% discount)"""
        items = [{"quantity": 8, "price": 10}]
        self.assertEqual(calculate_order_total(items), 0.95 * 8 * 10)

    def test_calculate_order_total_single_item_10_percent_discount(self):
        """Checks order total for single item with quantity > 10 (10% discount)"""
        items = [{"quantity": 15, "price": 10}]
        self.assertEqual(calculate_order_total(items), 0.9 * 15 * 10)

    def test_calculate_order_total_multiple_items(self):
        """Checks order total for multiple items with different quantities"""
        items = [
            {"quantity": 3, "price": 10},
            {"quantity": 8, "price": 20},
            {"quantity": 12, "price": 5},
        ]
        expected = (3 * 10) + (0.95 * 8 * 20) + (0.9 * 12 * 5)
        self.assertEqual(calculate_order_total(items), expected)

    def test_calculate_order_total_empty_list(self):
        """Checks order total for empty items list"""
        items = []
        self.assertEqual(calculate_order_total(items), 0)


class TestCalculateItemsShippingCost(unittest.TestCase):
    """Tests for the calculate_items_shipping_cost function."""

    def test_calculate_items_shipping_cost_standard_light(self):
        """Checks standard shipping cost for light items (weight <= 5)"""
        items = [{"weight": 3}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_calculate_items_shipping_cost_standard_medium(self):
        """Checks standard shipping cost for medium items (5 < weight <= 10)"""
        items = [{"weight": 7}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_standard_heavy(self):
        """Checks standard shipping cost for heavy items (weight > 10)"""
        items = [{"weight": 12}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_calculate_items_shipping_cost_express_light(self):
        """Checks express shipping cost for light items (weight <= 5)"""
        items = [{"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_calculate_items_shipping_cost_express_medium(self):
        """Checks express shipping cost for medium items (5 < weight <= 10)"""
        items = [{"weight": 8}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_calculate_items_shipping_cost_express_heavy(self):
        """Checks express shipping cost for heavy items (weight > 10)"""
        items = [{"weight": 15}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_calculate_items_shipping_cost_multiple_items(self):
        """Checks shipping cost calculation with multiple items"""
        items = [{"weight": 3}, {"weight": 4}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_calculate_items_shipping_cost_invalid_method(self):
        """Checks that invalid shipping method raises ValueError"""
        items = [{"weight": 5}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "invalid")


class TestValidateLogin(unittest.TestCase):
    """Tests for the validate_login function."""

    def test_validate_login_valid_credentials(self):
        """Checks valid login credentials"""
        self.assertEqual(validate_login("admin", "password123"), "Login Successful")

    def test_validate_login_short_username(self):
        """Checks login with username too short (< 5)"""
        self.assertEqual(validate_login("abc", "password123"), "Login Failed")

    def test_validate_login_long_username(self):
        """Checks login with username too long (> 20)"""
        self.assertEqual(validate_login("a" * 21, "password123"), "Login Failed")

    def test_validate_login_short_password(self):
        """Checks login with password too short (< 8)"""
        self.assertEqual(validate_login("admin", "pass123"), "Login Failed")

    def test_validate_login_long_password(self):
        """Checks login with password too long (> 15)"""
        self.assertEqual(validate_login("admin", "a" * 16), "Login Failed")

    def test_validate_login_boundary_username_length(self):
        """Checks login with username at boundary (5 and 20 characters)"""
        self.assertEqual(validate_login("admin", "password123"), "Login Successful")
        self.assertEqual(validate_login("a" * 20, "password123"), "Login Successful")


class TestVerifyAge(unittest.TestCase):
    """Tests for the verify_age function."""

    def test_verify_age_eligible(self):
        """Checks if age is within eligible range (18-65)"""
        self.assertEqual(verify_age(25), "Eligible")

    def test_verify_age_eligible_minimum(self):
        """Checks if age at minimum eligible boundary (18)"""
        self.assertEqual(verify_age(18), "Eligible")

    def test_verify_age_eligible_maximum(self):
        """Checks if age at maximum eligible boundary (65)"""
        self.assertEqual(verify_age(65), "Eligible")

    def test_verify_age_too_young(self):
        """Checks if age is below eligible range"""
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_verify_age_too_old(self):
        """Checks if age is above eligible range"""
        self.assertEqual(verify_age(66), "Not Eligible")


class TestCategorizeProduct(unittest.TestCase):
    """Tests for the categorize_product function."""

    def test_categorize_product_category_a(self):
        """Checks product categorization in Category A (10-50)"""
        self.assertEqual(categorize_product(30), "Category A")

    def test_categorize_product_category_a_minimum(self):
        """Checks product categorization at Category A minimum boundary (10)"""
        self.assertEqual(categorize_product(10), "Category A")

    def test_categorize_product_category_a_maximum(self):
        """Checks product categorization at Category A maximum boundary (50)"""
        self.assertEqual(categorize_product(50), "Category A")

    def test_categorize_product_category_b(self):
        """Checks product categorization in Category B (51-100)"""
        self.assertEqual(categorize_product(75), "Category B")

    def test_categorize_product_category_c(self):
        """Checks product categorization in Category C (101-200)"""
        self.assertEqual(categorize_product(150), "Category C")

    def test_categorize_product_category_d(self):
        """Checks product categorization in Category D (> 200)"""
        self.assertEqual(categorize_product(250), "Category D")

    def test_categorize_product_below_minimum(self):
        """Checks product categorization for price below minimum (< 10)"""
        self.assertEqual(categorize_product(5), "Category D")


class TestValidateEmail(unittest.TestCase):
    """Tests for the validate_email function."""

    def test_validate_email_valid(self):
        """Checks valid email validation"""
        self.assertEqual(validate_email("user@example.com"), "Valid Email")

    def test_validate_email_minimum_length(self):
        """Checks email validation at minimum length boundary (5)"""
        self.assertEqual(validate_email("a@b.c"), "Valid Email")

    def test_validate_email_maximum_length(self):
        """Checks email validation at maximum length boundary (50)"""
        self.assertEqual(validate_email("a" * 38 + "@example.com"), "Valid Email")

    def test_validate_email_too_short(self):
        """Checks email validation for too short email (< 5)"""
        self.assertEqual(validate_email("ab@c"), "Invalid Email")

    def test_validate_email_too_long(self):
        """Checks email validation for too long email (> 50)"""
        self.assertEqual(validate_email("a" * 45 + "@example.com"), "Invalid Email")

    def test_validate_email_missing_at(self):
        """Checks email validation for missing @ symbol"""
        self.assertEqual(validate_email("userexample.com"), "Invalid Email")

    def test_validate_email_missing_dot(self):
        """Checks email validation for missing dot symbol"""
        self.assertEqual(validate_email("user@examplecom"), "Invalid Email")


class TestCelsiusToFahrenheit(unittest.TestCase):
    """Tests for the celsius_to_fahrenheit function."""

    def test_celsius_to_fahrenheit_positive(self):
        """Checks Celsius to Fahrenheit conversion for positive temperature"""
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_freezing(self):
        """Checks Celsius to Fahrenheit conversion at freezing point"""
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_celsius_to_fahrenheit_boiling(self):
        """Checks Celsius to Fahrenheit conversion at boiling point"""
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_negative(self):
        """Checks Celsius to Fahrenheit conversion for negative temperature"""
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_celsius_to_fahrenheit_minimum_boundary(self):
        """Checks Celsius to Fahrenheit conversion at minimum boundary (-100)"""
        self.assertEqual(celsius_to_fahrenheit(-100), -148)

    def test_celsius_to_fahrenheit_maximum_boundary(self):
        """Checks Celsius to Fahrenheit conversion at maximum boundary (100)"""
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_celsius_to_fahrenheit_out_of_range_low(self):
        """Checks Celsius to Fahrenheit conversion for temperature below minimum"""
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_celsius_to_fahrenheit_out_of_range_high(self):
        """Checks Celsius to Fahrenheit conversion for temperature above maximum"""
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")


class TestValidateCreditCard(unittest.TestCase):
    """Tests for the validate_credit_card function."""

    def test_validate_credit_card_valid_13_digits(self):
        """Checks credit card validation for valid 13-digit card"""
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_validate_credit_card_valid_16_digits(self):
        """Checks credit card validation for valid 16-digit card"""
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_validate_credit_card_too_short(self):
        """Checks credit card validation for card with too few digits (< 13)"""
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_validate_credit_card_too_long(self):
        """Checks credit card validation for card with too many digits (> 16)"""
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")

    def test_validate_credit_card_non_numeric(self):
        """Checks credit card validation for card with non-numeric characters"""
        self.assertEqual(validate_credit_card("123456789012A"), "Invalid Card")


class TestValidateDate(unittest.TestCase):
    """Tests for the validate_date function."""

    def test_validate_date_valid(self):
        """Checks valid date validation"""
        self.assertEqual(validate_date(2024, 5, 15), "Valid Date")

    def test_validate_date_leap_year(self):
        """Checks valid date for leap year"""
        self.assertEqual(validate_date(2020, 2, 29), "Valid Date")

    def test_validate_date_year_minimum(self):
        """Checks date validation at minimum year boundary (1900)"""
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")

    def test_validate_date_year_maximum(self):
        """Checks date validation at maximum year boundary (2100)"""
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")

    def test_validate_date_year_too_low(self):
        """Checks date validation for year below minimum (< 1900)"""
        self.assertEqual(validate_date(1899, 1, 1), "Invalid Date")

    def test_validate_date_year_too_high(self):
        """Checks date validation for year above maximum (> 2100)"""
        self.assertEqual(validate_date(2101, 1, 1), "Invalid Date")

    def test_validate_date_month_too_low(self):
        """Checks date validation for month below minimum (< 1)"""
        self.assertEqual(validate_date(2024, 0, 15), "Invalid Date")

    def test_validate_date_month_too_high(self):
        """Checks date validation for month above maximum (> 12)"""
        self.assertEqual(validate_date(2024, 13, 15), "Invalid Date")

    def test_validate_date_day_too_low(self):
        """Checks date validation for day below minimum (< 1)"""
        self.assertEqual(validate_date(2024, 5, 0), "Invalid Date")

    def test_validate_date_day_too_high(self):
        """Checks date validation for day above maximum (> 31)"""
        self.assertEqual(validate_date(2024, 5, 32), "Invalid Date")


class TestCheckFlightEligibility(unittest.TestCase):
    """Tests for the check_flight_eligibility function."""

    def test_check_flight_eligibility_age_in_range(self):
        """Checks flight eligibility for age within eligible range"""
        self.assertEqual(check_flight_eligibility(30, False), "Eligible to Book")

    def test_check_flight_eligibility_age_minimum(self):
        """Checks flight eligibility at minimum age boundary (18)"""
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")

    def test_check_flight_eligibility_age_maximum(self):
        """Checks flight eligibility at maximum age boundary (65)"""
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    def test_check_flight_eligibility_frequent_flyer(self):
        """Checks flight eligibility for frequent flyer regardless of age"""
        self.assertEqual(check_flight_eligibility(10, True), "Eligible to Book")

    def test_check_flight_eligibility_too_young_no_frequent_flyer(self):
        """Checks flight eligibility for person too young and not a frequent flyer"""
        self.assertEqual(check_flight_eligibility(10, False), "Not Eligible to Book")

    def test_check_flight_eligibility_too_old_no_frequent_flyer(self):
        """Checks flight eligibility for person too old and not a frequent flyer"""
        self.assertEqual(check_flight_eligibility(70, False), "Not Eligible to Book")


class TestValidateUrl(unittest.TestCase):
    """Tests for the validate_url function."""

    def test_validate_url_https(self):
        """Checks URL validation for HTTPS URL"""
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_validate_url_http(self):
        """Checks URL validation for HTTP URL"""
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_validate_url_no_protocol(self):
        """Checks URL validation for URL without protocol"""
        self.assertEqual(validate_url("example.com"), "Invalid URL")

    def test_validate_url_too_long(self):
        """Checks URL validation for URL longer than 255 characters"""
        long_url = "https://" + ("a" * 255)
        self.assertEqual(validate_url(long_url), "Invalid URL")

    def test_validate_url_max_length(self):
        """Checks URL validation for URL at maximum length (255)"""
        url = "https://" + "a" * 240
        self.assertEqual(validate_url(url), "Valid URL")


class TestCalculateQuantityDiscount(unittest.TestCase):
    """Tests for the calculate_quantity_discount function."""

    def test_calculate_quantity_discount_no_discount(self):
        """Checks quantity discount for 1-5 items (no discount)"""
        self.assertEqual(calculate_quantity_discount(3), "No Discount")

    def test_calculate_quantity_discount_5_percent(self):
        """Checks quantity discount for 6-10 items (5% discount)"""
        self.assertEqual(calculate_quantity_discount(8), "5% Discount")

    def test_calculate_quantity_discount_10_percent(self):
        """Checks quantity discount for items > 10 (10% discount)"""
        self.assertEqual(calculate_quantity_discount(15), "10% Discount")

    def test_calculate_quantity_discount_boundary_1(self):
        """Checks quantity discount at boundary between no discount and 5% (5 vs 6)"""
        self.assertEqual(calculate_quantity_discount(5), "No Discount")
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_calculate_quantity_discount_boundary_2(self):
        """Checks quantity discount at boundary between 5% and 10% (10 vs 11)"""
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")


class TestCheckFileSize(unittest.TestCase):
    """Tests for the check_file_size function."""

    def test_check_file_size_valid_small(self):
        """Checks file size validation for small file"""
        self.assertEqual(check_file_size(500000), "Valid File Size")

    def test_check_file_size_valid_maximum(self):
        """Checks file size validation at maximum boundary (1 MB = 1048576 bytes)"""
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_check_file_size_zero(self):
        """Checks file size validation for zero-byte file"""
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_check_file_size_too_large(self):
        """Checks file size validation for file larger than 1 MB"""
        self.assertEqual(check_file_size(1048577), "Invalid File Size")

    def test_check_file_size_negative(self):
        """Checks file size validation for negative file size"""
        self.assertEqual(check_file_size(-100), "Invalid File Size")


class TestCheckLoanEligibility(unittest.TestCase):
    """Tests for the check_loan_eligibility function."""

    def test_check_loan_eligibility_low_income(self):
        """Checks loan eligibility for income below minimum (< 30000)"""
        self.assertEqual(check_loan_eligibility(20000, 750), "Not Eligible")

    def test_check_loan_eligibility_standard_loan_high_score(self):
        """Checks loan eligibility for standard loan with good credit (30000-60000, score > 700)"""
        self.assertEqual(check_loan_eligibility(50000, 750), "Standard Loan")

    def test_check_loan_eligibility_secured_loan_low_score(self):
        """Checks loan eligibility for secured loan with poor credit (30000-60000, score <= 700)"""
        self.assertEqual(check_loan_eligibility(50000, 650), "Secured Loan")

    def test_check_loan_eligibility_premium_loan(self):
        """Checks loan eligibility for premium loan with excellent credit (> 60000, score > 750)"""
        self.assertEqual(check_loan_eligibility(80000, 800), "Premium Loan")

    def test_check_loan_eligibility_standard_loan_high_income(self):
        """Checks loan eligibility for high income
        but not excellent credit (> 60000, score <= 750)"""
        self.assertEqual(check_loan_eligibility(80000, 700), "Standard Loan")


class TestCalculateShippingCost(unittest.TestCase):
    """Tests for the calculate_shipping_cost function."""

    def test_calculate_shipping_cost_small_light(self):
        """Checks shipping cost for small light package"""
        self.assertEqual(calculate_shipping_cost(0.5, 5, 5, 5), 5)

    def test_calculate_shipping_cost_medium(self):
        """Checks shipping cost for medium package"""
        self.assertEqual(calculate_shipping_cost(2, 15, 15, 15), 10)

    def test_calculate_shipping_cost_large_heavy(self):
        """Checks shipping cost for large heavy package"""
        self.assertEqual(calculate_shipping_cost(10, 50, 50, 50), 20)

    def test_calculate_shipping_cost_weight_boundary_1(self):
        """Checks shipping cost at weight boundary (1 vs 1.1)"""
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)
        self.assertEqual(calculate_shipping_cost(1.1, 11, 11, 11), 10)

    def test_calculate_shipping_cost_weight_boundary_2(self):
        """Checks shipping cost at weight boundary (5 vs 5.1)"""
        self.assertEqual(calculate_shipping_cost(5, 30, 30, 30), 10)
        self.assertEqual(calculate_shipping_cost(5.1, 35, 35, 35), 20)


class TestGradeQuiz(unittest.TestCase):
    """Tests for the grade_quiz function."""

    def test_grade_quiz_pass(self):
        """Checks quiz grading for pass (correct >= 7, incorrect <= 2)"""
        self.assertEqual(grade_quiz(8, 1), "Pass")

    def test_grade_quiz_conditional_pass(self):
        """Checks quiz grading for conditional pass (correct >= 5, incorrect <= 3)"""
        self.assertEqual(grade_quiz(6, 2), "Conditional Pass")

    def test_grade_quiz_fail(self):
        """Checks quiz grading for fail"""
        self.assertEqual(grade_quiz(4, 4), "Fail")

    def test_grade_quiz_perfect_score(self):
        """Checks quiz grading for perfect score"""
        self.assertEqual(grade_quiz(10, 0), "Pass")

    def test_grade_quiz_boundary_pass(self):
        """Checks quiz grading at pass boundary (7 correct, 2 incorrect)"""
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_grade_quiz_boundary_conditional(self):
        """Checks quiz grading at conditional pass boundary (5 correct, 3 incorrect)"""
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")


class TestAuthenticateUser(unittest.TestCase):
    """Tests for the authenticate_user function."""

    def test_authenticate_user_admin(self):
        """Checks authentication for admin user"""
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_authenticate_user_valid_user(self):
        """Checks authentication for valid regular user"""
        self.assertEqual(authenticate_user("validuser", "password123"), "User")

    def test_authenticate_user_short_username(self):
        """Checks authentication for user with short username (< 5)"""
        self.assertEqual(authenticate_user("abc", "password123"), "Invalid")

    def test_authenticate_user_short_password(self):
        """Checks authentication for user with short password (< 8)"""
        self.assertEqual(authenticate_user("validuser", "pass123"), "Invalid")

    def test_authenticate_user_wrong_admin_password(self):
        """Checks authentication for admin with wrong password"""
        self.assertEqual(authenticate_user("admin", "wrongpass"), "User")

    def test_authenticate_user_boundary_credentials(self):
        """Checks authentication at boundary (5 char username, 8 char password)"""
        self.assertEqual(authenticate_user("abcde", "password"), "User")


class TestGetWeatherAdvisory(unittest.TestCase):
    """Tests for the get_weather_advisory function."""

    def test_get_weather_advisory_high_temp_humidity(self):
        """Checks weather advisory for high temperature and humidity"""
        self.assertEqual(
            get_weather_advisory(35, 80),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_get_weather_advisory_low_temperature(self):
        """Checks weather advisory for low temperature"""
        self.assertEqual(get_weather_advisory(-10, 50), "Low Temperature. Bundle Up!")

    def test_get_weather_advisory_no_advisory(self):
        """Checks weather advisory for normal conditions"""
        self.assertEqual(get_weather_advisory(20, 50), "No Specific Advisory")

    def test_get_weather_advisory_high_temp_low_humidity(self):
        """Checks weather advisory for high temperature but low humidity"""
        self.assertEqual(get_weather_advisory(35, 60), "No Specific Advisory")

    def test_get_weather_advisory_low_temp_edge_case(self):
        """
        Checks weather advisory at freezing point (Using 0 as temperature)
        NO DEBERIA DE SER LOW TEMPERATURE????
        """
        self.assertEqual(get_weather_advisory(0, 50), "No Specific Advisory")
